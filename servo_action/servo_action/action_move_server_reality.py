#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ros2 run servo_action action_move_server_reality

import time

import rclpy                                      # ROS2 Python接口库
from rclpy.node   import Node                     # ROS2 节点类
from rclpy.action import ActionServer             
from control_msgs.action import FollowJointTrajectory  
from moveit_msgs.msg import DisplayTrajectory                 
from trajectory_msgs.msg import JointTrajectoryPoint
from dobot_msgs_v3.srv import *                               
import time
import os


class MoveCircleActionServer(Node):
    def __init__(self, name):
        super().__init__(name)                   # ROS2节点父类初始化
        mane = os.getenv("DOBOT_TYPE")
        self._action_server = ActionServer(      # 创建动作服务器（接口类型、动作名、回调函数）
            self,
            FollowJointTrajectory,
            f'{mane}_group_controller/follow_joint_trajectory',
            self.execute_callback)
        self.sub = self.create_subscription(\
            DisplayTrajectory, "/display_planned_path", self.listener_callback, 10)        # 创建订阅者对象（消息类型、话题名、订阅者回调函数、队列长度）
        self.Trajectory = False
        self.EnableRobot_l = self.create_client(EnableRobot,'/dobot_bringup_v3/srv/EnableRobot')
        self.ServoJ_l = self.create_client(ServoJ,'/dobot_bringup_v3/srv/ServoJ')
        while not self.EnableRobot_l.wait_for_service(timeout_sec=1.0):                  # 循环等待服务器端成功启动
            self.get_logger().info('service not available, waiting again...') 

    def listener_callback(self, msg): 
        self.adc = []                                              
        for i in msg.trajectory[0].joint_trajectory.points:        
            acd = []
            for ii in i.positions:
                acd.append(180*ii/3.14159)
            self.adc.append(acd)
            print(f"Planning location:{acd}")
        self.Trajectory = True
            

    def execute_callback(self, goal_handle):           
        if self.Trajectory:
            for i in self.adc:
               self.ServoJ_C(i[0],i[1],i[2],i[3],i[4],i[5])
               print(f"ServoJ:{i}")
               time.sleep(0.35)
            self.Trajectory = False
        else:
            print("No data.....")
        goal_handle.succeed()                           # 动作执行成功
        result = FollowJointTrajectory.Result()        
        result.error_code=0                           
        return result                                 
    def ServoJ_C(self, j1, j2, j3, j4, j5,j6):  # 运动指令
            P1 = ServoJ.Request()
            P1.j1 = float(j1)
            P1.j2 = float(j2)
            P1.j3 = float(j3)
            P1.j4 = float(j4)
            P1.j5 = float(j5)
            P1.j6 = float(j6)
            P1.t = float(0.4)
            response = self.ServoJ_l.call_async(P1)
    

def main(args=None):                                       # ROS2节点主入口main函数
    rclpy.init(args=args)                                  
    node = MoveCircleActionServer("action_move_server")   
    rclpy.spin(node)                                       
    node.destroy_node()                                    
    rclpy.shutdown()                                       # 关闭ROS2 Python接口
