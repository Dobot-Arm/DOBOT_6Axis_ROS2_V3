#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

class DobotApi:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket_dobot = 0

        if self.port == 29999 or self.port == 30003:
            self.socket_dobot = socket.socket()
            self.socket_dobot.connect((self.ip, self.port))

        else:
            print(f"Connect to dashboard server need use port {self.port} !")

    def send_data(self, string):
        print(string)
        self.socket_dobot.send(str.encode(string, 'utf-8'))

    def wait_reply(self):
        data = self.socket_dobot.recv(1024)
        data_str = str(data, encoding="utf-8")
        return data_str

    def close(self):
        """
        Close the port
        """
        if (self.socket_dobot != 0):
            self.socket_dobot.close()

    def sendRecvMsg(self, string):
        self.send_data(string)
        return self.wait_reply()



# 控制及运动指令接口类
# Control and motion command interface


class DobotApiDashboard(DobotApi):

    def EnableRobot(self,*dynParams):
        """
        Enable the robot
        """
        string = "EnableRobot("+str(dynParams[0][0])+")"
        return self.sendRecvMsg(string)

    def DisableRobot(self):
        """
        Disabled the robot
        """
        string = "DisableRobot()"
        return self.sendRecvMsg(string)

    def ClearError(self):
        """
        Clear controller alarm information
        """
        string = "ClearError()"
        return self.sendRecvMsg(string)

    def ResetRobot(self):
        """
        Robot stop
        """
        string = "ResetRobot()"
        return self.sendRecvMsg(string)

    def SpeedFactor(self, speed):
        """
        Setting the Global rate   
        speed:Rate value(Value range:1~100)
        """
        string = "SpeedFactor({:d})".format(speed)
        return self.sendRecvMsg(string)

    def User(self, index):
        """
        Select the calibrated user coordinate system
        index : Calibrated index of user coordinates
        """
        string = "User({:d})".format(index)
        return self.sendRecvMsg(string)

    def Tool(self, index):
        """
        Select the calibrated tool coordinate system
        index : Calibrated index of tool coordinates
        """
        string = "Tool({:d})".format(index)
        return self.sendRecvMsg(string)

    def RobotMode(self):
        """
        View the robot status
        """
        string = "RobotMode()"
        return self.sendRecvMsg(string)

    def PayLoad(self, weight, inertia):
        """
        Setting robot load
        weight : The load weight
        inertia: The load moment of inertia
        """
        string = "PayLoad({:f},{:f})".format(weight, inertia)
        return self.sendRecvMsg(string)

    def DO(self, index, status):
        """
        Set digital signal output (Queue instruction)
        index : Digital output index (Value range:1~24)
        status : Status of digital signal output port(0:Low level，1:High level
        """
        string = "DO({:d},{:d})".format(index, status)
        return self.sendRecvMsg(string)

    def AccJ(self, speed):
        """
        Set joint acceleration ratio (Only for MovJ, MovJIO, MovJR, JointMovJ commands)
        speed : Joint acceleration ratio (Value range:1~100)
        """
        string = "AccJ({:d})".format(speed)
        return self.sendRecvMsg(string)

    def AccL(self, speed):
        """
        Set the coordinate system acceleration ratio (Only for MovL, MovLIO, MovLR, Jump, Arc, Circle commands)
        speed : Cartesian acceleration ratio (Value range:1~100)
        """
        string = "AccL({:d})".format(speed)
        return self.sendRecvMsg(string)

    def SpeedJ(self, speed):
        """
        Set joint speed ratio (Only for MovJ, MovJIO, MovJR, JointMovJ commands)
        speed : Joint velocity ratio (Value range:1~100)
        """
        string = "SpeedJ({:d})".format(speed)
        return self.sendRecvMsg(string)

    def SpeedL(self, speed):
        """
        Set the cartesian acceleration ratio (Only for MovL, MovLIO, MovLR, Jump, Arc, Circle commands)
        speed : Cartesian acceleration ratio (Value range:1~100)
        """
        string = "SpeedL({:d})".format(speed)
        return self.sendRecvMsg(string)

    def Arch(self, index):
        """
        Set the Jump gate parameter index (This index contains: start point lift height, maximum lift height, end point drop height)
        index : Parameter index (Value range:0~9)
        """
        string = "Arch({:d})".format(index)
        return self.sendRecvMsg(string)

    def CP(self, ratio):
        """
        Set smooth transition ratio
        ratio : Smooth transition ratio (Value range:1~100)
        """
        string = "CP({:d})".format(ratio)
        return self.sendRecvMsg(string)

    def LimZ(self, value):
        """
        Set the maximum lifting height of door type parameters
        value : Maximum lifting height (Highly restricted:Do not exceed the limit position of the z-axis of the manipulator)
        """
        string = "LimZ({:d})".format(value)
        return self.sendRecvMsg(string)

    def RunScript(self, project_name):
        """
        Run the script file
        project_name ：Script file name
        """
        string = "RunScript({:s})".format(project_name)
        return self.sendRecvMsg(string)

    def StopScript(self):
        """
        Stop scripts
        """
        string = "StopScript()"
        return self.sendRecvMsg(string)

    def PauseScript(self):
        """
        Pause the script
        """
        string = "PauseScript()"
        return self.sendRecvMsg(string)

    def ContinueScript(self):
        """
        Continue running the script
        """
        string = "ContinueScript()"
        return self.sendRecvMsg(string)

    def GetHoldRegs(self, id, addr, count, type=None):
        if type is not None:  
          string = "GetHoldRegs({:d},{:d},{:d},{:s})".format(
            id, addr, count, type)
        else:
          string = "GetHoldRegs({:d},{:d},{:d})".format(
            id, addr, count)   
        return self.sendRecvMsg(string)

    def SetHoldRegs(self, id, addr, count, table, type=None):
        if type is not None:
          string = "SetHoldRegs({:d},{:d},{:d},{:d},{:s})".format(
            id, addr, count, table, type)
        else:
          string = "SetHoldRegs({:d},{:d},{:d},{:d})".format(
            id, addr, count, table)
        return self.sendRecvMsg(string)

    def GetErrorID(self):
        """
        Get robot error code
        """
        string = "GetErrorID()"
        return self.sendRecvMsg(string)
    
    
    def DOExecute(self,offset1,offset2):
        string = "DOExecute({:d},{:d}".format(offset1,offset2)+")"
        return self.sendRecvMsg(string)
      
    def ToolDO(self,offset1,offset2):
        string = "ToolDO({:d},{:d}".format(offset1,offset2)+")"
        return self.sendRecvMsg(string)

    def ToolDOExecute(self,offset1,offset2):
        string = "ToolDOExecute({:d},{:d}".format(offset1,offset2)+")"
        return self.sendRecvMsg(string)

    def  SetArmOrientation(self,offset1):
        string = "SetArmOrientation({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)

    def SetPayload(self, weight, inertia):
        string = "SetPayLoad({:f},{:f})".format(weight, inertia)
        return self.sendRecvMsg(string)

    def PositiveSolution(self,offset1,offset2,offset3,offset4,user,tool):   
        string = "PositiveSolution({:f},{:f},{:f},{:f},{:d},{:d}".format(offset1,offset2,offset3,offset4,user,tool)+")"
        return self.sendRecvMsg(string)

    def InverseSolution(self,offset1,offset2,offset3,offset4,user,tool,*dynParams):       
        string = "InverseSolution({:f},{:f},{:f},{:f},{:d},{:d}".format(offset1,offset2,offset3,offset4,user,tool)
        for params in dynParams:
            print(type(params), params)
            string = string + repr(params)
        string = string + ")"
        return self.sendRecvMsg(string)     

    def SetCollisionLevel(self,offset1):
        string = "SetCollisionLevel({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)

    def  GetAngle(self):
        string = "GetAngle()"
        return self.sendRecvMsg(string)

    def  GetPose(self,User=0,Tool=0):
        string = "GetPose(User={:d},Tool={:d})".format(User,Tool)
        return self.sendRecvMsg(string)
    
    def EmergencyStop(self):
        string = "EmergencyStop()"
        return self.sendRecvMsg(string)


    def ModbusCreate(self,ip,port,slave_id,isRTU):
        string ="ModbusCreate({:s},{:d},{:d},{:d}".format(ip,port,slave_id,isRTU)+")"
        return self.sendRecvMsg(string)
    
    def ModbusClose(self,offset1):
        string = "ModbusClose({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)

    def GetInBits(self,offset1,offset2,offset3):
        string = "GetInBits({:d},{:d},{:d}".format(offset1,offset2,offset3)+")"
        return self.sendRecvMsg(string)        

    def GetInRegs(self,offset1,offset2,offset3,*dynParams):
        string = "GetInRegs({:d},{:d},{:d}".format(offset1,offset2,offset3)
        for params in dynParams:
            print(type(params), params)
            string = string + params[0]
        string = string + ")"
        return self.sendRecvMsg(string)  

    def GetCoils(self,offset1,offset2,offset3):
        string = "GetCoils({:d},{:d},{:d}".format(offset1,offset2,offset3)+")"
        return self.sendRecvMsg(string)          

    def SetCoils(self,offset1,offset2,offset3,offset4):
        string = "SetCoils({:d},{:d},{:d}".format(offset1,offset2,offset3)+","+ repr(offset4)+")"
        print(str(offset4))
        return self.sendRecvMsg(string)              

    def DI(self,offset1):
        string = "DI({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)        

    def ToolDI(self,offset1):
        string = "DI({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)   

    def DOGroup(self,*dynParams):
        string = "DOGroup("
        for params in dynParams[0]:
            string = string + str(params)+","
        string =string+ ")"   
        return self.wait_reply()  

    def BrakeControl(self,offset1,offset2): 
        string = "BrakeControl({:d},{:d}".format(offset1,offset2)+")"
        return self.sendRecvMsg(string)             

    def StartDrag(self):
        string = "StartDrag()"
        return self.sendRecvMsg(string)      

    def StopDrag(self):
        string = "StopDrag()"
        return self.sendRecvMsg(string)           

    def LoadSwitch(self,offset1):    
        string = "LoadSwitch({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)                                                       

    def wait(self):
        string = "wait()"
        return self.sendRecvMsg(string)

    def pause(self):
        string = "pause()"
        return self.sendRecvMsg(string)

    def Continue(self):
        string = "continue()"
        return self.sendRecvMsg(string)
    
class DobotApiMove(DobotApi):
    """
    Define class dobot_api_move to establish a connection to Dobot
    """

    def MovJ(self, x, y, z, rx,ry,rz,*dynParams):
        """
        Joint motion interface (point-to-point motion mode)
        x: A number in the Cartesian coordinate system x
        y: A number in the Cartesian coordinate system y
        z: A number in the Cartesian coordinate system z
        r: A number in the Cartesian coordinate system R
        """
        string = "MovJ({:f},{:f},{:f},{:f},{:f},{:f}".format(
            x, y, z, rx,ry,rz)
        for params in dynParams[0]:
             string =string+ ","+ str(params)
        string =string+ ")" 
        print(string)  
        return self.sendRecvMsg(string)

    def MovL(self, x, y, z, rx,ry,rz,*dynParams):
        """
        Coordinate system motion interface (linear motion mode)
        x: A number in the Cartesian coordinate system x
        y: A number in the Cartesian coordinate system y
        z: A number in the Cartesian coordinate system z
        r: A number in the Cartesian coordinate system R
        """
        string = "MovL({:f},{:f},{:f},{:f},{:f},{:f}".format(
            x, y, z, rx,ry,rz)
        for params in dynParams[0]:
             string =string+ ","+ str(params)
        string =string+ ")" 
        print(string) 
        return self.sendRecvMsg(string)

    def JointMovJ(self, j1, j2, j3, j4,j5,j6,*dynParams):
        """
        Joint motion interface (linear motion mode)
        j1~j6:Point position values on each joint
        """
        string = "JointMovJ({:f},{:f},{:f},{:f},{:f},{:f}".format(
            j1, j2, j3, j4,j5,j6)
        for params in dynParams[0]:
            string =string+ ","+ str(params)
        string =string+ ")" 
        print(string)
        return self.sendRecvMsg(string)
    
    def ServoJ(self, j1, j2, j3, j4,j5,j6,t,*dynParams):
        string = "ServoJ({:f},{:f},{:f},{:f},{:f},{:f},t={:f}".format(
            j1,j2,j3,j4,j5,j6,t)
        for params in dynParams[0]:
             string =string+ ","+ str(params)
        string =string+ ")" 
        print(string) 
        return self.sendRecvMsg(string)

    def ServoP(self, x, y, z, rx,ry,rz):
        string = "ServoP({:f},{:f},{:f},{:f},{:f},{:f})".format(
            x, y, z, rx,ry,rz)
        print(string) 
        return self.sendRecvMsg(string)

    def Jump(self):
        print("待定")

    def RelMovJ(self, offset1, offset2, offset3,offset4, offset5,offset6,*dynParams):
        """
        Offset motion interface (point-to-point motion mode)
        j1~j6:Point position values on each joint
        """
        string = "RelMovJ({:f},{:f},{:f},{:f},{:f},{:f}".format(
            offset1, offset2, offset3,offset4, offset5,offset6)
        for params in dynParams[0]:
            string =string+ ","+ str(params)
        string =string+ ")" 
        return self.sendRecvMsg(string)

    def RelMovL(self, offset1, offset2, offset3,offset4, offset5,offset6,*dynParams):
        """
        Offset motion interface (point-to-point motion mode)
        x: Offset in the Cartesian coordinate system x
        y: offset in the Cartesian coordinate system y
        z: Offset in the Cartesian coordinate system Z
        r: Offset in the Cartesian coordinate system R
        """
        string = "RelMovL({:f},{:f},{:f},{:f},{:f},{:f}".format(offset1, offset2, offset3,offset4, offset5,offset6)
        for params in dynParams[0]:
            string =string+ ","+ str(params)
        string =string+ ")" 
        return self.sendRecvMsg(string)

    def MovLIO(self, x, y, z, rx,ry,rz, *dynParams):
        # example： MovLIO(0,50,0,0,0,0,(0,50,1,0),(1,1,2,1))
        string = "MovLIO({:f},{:f},{:f},{:f},{:f},{:f}".format(
            x, y, z, rx,ry,rz)
        for params in dynParams[0]:
            string =string+ ","+ str(params)
        string =string+ ")" 
        return self.sendRecvMsg(string)

    def MovJIO(self, x, y, z, rx,ry,rz, *dynParams):
        # example： MovJIO(0,50,0,0,0,0,(0,50,1,0),(1,1,2,1))
        string = "MovJIO({:f},{:f},{:f},{:f},{:f},{:f}".format(
            x, y, z, rx,ry,rz)
        for params in dynParams[0]:
            string =string+ ","+ str(params)
        string =string+ ")" 
        print(string)
        return self.sendRecvMsg(string)

    def Arc(self, x1, y1, z1, rx1,ry1,rz1,x2, y2, z2, rx2,ry2,rz2,*dynParams):
        """
        Circular motion instruction
        x1, y1, z1, r1 :Is the point value of intermediate point coordinates
        x2, y2, z2, r2 :Is the value of the end point coordinates
        Note: This instruction should be used together with other movement instructions
        """
        string = "Arc({:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f}".format(
            x1, y1, z1, rx1,ry1,rz1,x2, y2, z2, rx2,ry2,rz2)
        for params in dynParams[0]:
            string =string+ ","+ str(params)
        string =string+ ")" 
        print(string)
        return self.sendRecvMsg(string)

    def Circle(self, x1, y1, z1, rx1,ry1,rz1,x2, y2, z2, rx2,ry2,rz2,count,*dynParams):
        """
        Full circle motion command
        count：Run laps
        x1, y1, z1, r1 :Is the point value of intermediate point coordinates
        x2, y2, z2, r2 :Is the value of the end point coordinates
        Note: This instruction should be used together with other movement instructions
        """
        string = "Circle({:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:d}".format(
             x1, y1, z1, rx1,ry1,rz1,x2, y2, z2, rx2,ry2,rz2, count)
        for params in dynParams:
            string = string + ","+ str(params)
        string = string + ")" 
        return self.sendRecvMsg(string)

    def MoveJog(self, axis_id=None, *dynParams):
        """
        Joint motion
        axis_id: Joint motion axis, optional string value:
            J1+ J2+ J3+ J4+ J5+ J6+
            J1- J2- J3- J4- J5- J6- 
            X+ Y+ Z+ Rx+ Ry+ Rz+ 
            X- Y- Z- Rx- Ry- Rz-
        *dynParams: Parameter Settings（coord_type, user_index, tool_index）
                    coord_type: 1: User coordinate 2: tool coordinate (default value is 1)
                    user_index: user index is 0 ~ 9 (default value is 0)
                    tool_index: tool index is 0 ~ 9 (default value is 0)
        """
        if axis_id is not None:
          string = "MoveJog({:s}".format(axis_id)
        else:
          string = "MoveJog("
        for params in dynParams[0]:
            string = string + ","+ str(params)
        string = string + ")" 
        return self.sendRecvMsg(string)


    def Sync(self):
        """
        The blocking program executes the queue instruction and returns after all the queue instructions are executed
        """
        string = "Sync()"
        return self.sendRecvMsg(string)

    def RelMovJUser(self, offset_1, offset_2, offset_3, offset_4, offset_5, offset_6, user, *dynParams):
        string = "RelMovJUser({:f},{:f},{:f},{:f},{:f},{:f}, {:d}".format(
            offset_1, offset_2, offset_3, offset_4, offset_5, offset_6, user)
        for params in dynParams[0]:
            string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)
    
    def RelMovJTool(self, offset_1, offset_2, offset_3, offset_4, offset_5, offset_6, tool, *dynParams):
        string = "RelMovJTool({:f},{:f},{:f},{:f},{:f},{:f}, {:d}".format(
            offset_1, offset_2, offset_3, offset_4, offset_5, offset_6, tool)
        for params in dynParams[0]:
            string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)

    def RelMovLUser(self, offset_1, offset_2, offset_3, offset_4, offset_5, offset_6, user, *dynParams):
        string = "RelMovLUser({:f},{:f},{:f},{:f},{:f},{:f}, {:d}".format(
            offset_1, offset_2, offset_3, offset_4, offset_5, offset_6, user)
        for params in dynParams[0]:
            string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)
    
    def RelMovLTool(self, offset_1, offset_2, offset_3, offset_4, offset_5, offset_6, tool, *dynParams):
        string = "RelMovLTool({:f},{:f},{:f},{:f},{:f},{:f}, {:d}".format(
            offset_1, offset_2, offset_3, offset_4, offset_5, offset_6, tool)
        for params in dynParams[0]:
            string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)
    

    def RelJointMovJ(self, offset1, offset2, offset3, offset4,offset5, offset6, *dynParams):
        """
        The relative motion command is carried out along the joint coordinate system of each axis, and the end motion mode is joint motion
        Offset motion interface (point-to-point motion mode)
        j1~j6:Point position values on each joint
        *dynParams: parameter Settings（speed_j, acc_j, user）
                    speed_j: Set Cartesian speed scale, value range: 1 ~ 100
                    acc_j: Set acceleration scale value, value range: 1 ~ 100
        """
        string = "RelJointMovJ({:f},{:f},{:f},{:f},{:f},{:f}".format(
            offset1, offset2, offset3, offset4,offset5, offset6)
        for params in dynParams:
           string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)
    
    def MovJExt(self, offset1, *dynParams):
        string = "MovJExt({:f}".format(
            offset1)
        for params in dynParams[0]:
           string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)

    def SyncAll(self):
        string = "SyncAll()"
        return self.sendRecvMsg(string)
