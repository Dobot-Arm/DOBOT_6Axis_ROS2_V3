cmake_minimum_required(VERSION 3.16)
project(dobot_msgs_v3)

# Default to C99
if (NOT CMAKE_C_STANDARD)
    set(CMAKE_C_STANDARD 99)
endif ()

# Default to C++17
if (NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 17)
endif ()

if (CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    add_compile_options(-Wall -Wextra -Wpedantic -fdiagnostics-color=always)
endif ()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(builtin_interfaces REQUIRED)

set(msg_files
        "msg/RobotStatus.msg"
        "msg/ToolVectorActual.msg"
        )

set(srv_files
      "srv/AccJ.srv"
      "srv/AccL.srv"
      "srv/AO.srv"
      "srv/AOExecute.srv"
      "srv/Arc.srv"
      "srv/Arch.srv"
      "srv/BrakeControl.srv"
      "srv/Circle.srv"
      "srv/ClearError.srv"
      "srv/Continues.srv"
      "srv/ContinueScript.srv"
      "srv/CP.srv"
      "srv/DI.srv"
      "srv/DigitalOutputs.srv"
      "srv/DisableRobot.srv"
      "srv/DO.srv"
      "srv/DOExecute.srv"
      "srv/DOGroup.srv"
      "srv/EmergencyStop.srv"
      "srv/EnableRobot.srv"
      "srv/GetAngle.srv"
      "srv/GetCoils.srv"
      "srv/GetErrorID.srv"
      "srv/GetHoldRegs.srv"
      "srv/GetInBits.srv"
      "srv/GetInRegs.srv"
      "srv/GetPose.srv"
      "srv/InverseSolution.srv"
      "srv/JointMovJ.srv"
      "srv/Jump.srv"
      "srv/LimZ.srv"
      "srv/LoadSwitch.srv"
      "srv/ModbusClose.srv"
      "srv/ModbusCreate.srv"
      "srv/MoveJog.srv"
      "srv/MovJ.srv"
      "srv/MovJExt.srv"
      "srv/MovJIO.srv"
      "srv/MovL.srv"
      "srv/MovLIO.srv"
      "srv/Pause.srv"
      "srv/PauseScript.srv"
      "srv/PayLoad.srv"
      "srv/PositiveSolution.srv"
      "srv/PowerOn.srv"
      "srv/RelJointMovJ.srv"
      "srv/RelMovJ.srv"
      "srv/RelMovJUser.srv"
      "srv/RelMovJTool.srv"
      "srv/RelMovL.srv"
      "srv/RelMovLUser.srv"
      "srv/RelMovLTool.srv"
      "srv/ResetRobot.srv"
      "srv/RobotMode.srv"
      "srv/RunScript.srv"
      "srv/ServoJ.srv"
      "srv/ServoP.srv"
      "srv/SetArmOrientation.srv"
      "srv/SetCoils.srv"
      "srv/SetCollisionLevel.srv"
      "srv/SetHoldRegs.srv"
      "srv/SetObstacleAvoid.srv"
      "srv/SetPayload.srv"
      "srv/SetSafeSkin.srv"
      "srv/SpeedFactor.srv"
      "srv/SpeedJ.srv"
      "srv/SpeedL.srv"
      "srv/StartDrag.srv"
      "srv/StartFCTrace.srv"
      "srv/StartPath.srv"
      "srv/StartTrace.srv"
      "srv/StopDrag.srv"
      "srv/StopmoveJog.srv"
      "srv/StopScript.srv"
      "srv/Sync.srv"
      "srv/SyncAll.srv"
      "srv/Tool.srv"
      "srv/ToolDI.srv"
      "srv/ToolDO.srv"
      "srv/ToolDOExecute.srv"
      "srv/User.srv"
      "srv/Wait.srv"

        )

rosidl_generate_interfaces(${PROJECT_NAME}
        ${msg_files} ${srv_files}
        DEPENDENCIES
        builtin_interfaces
        std_msgs
        )

ament_export_dependencies(rosidl_default_generators)
ament_export_dependencies(rosidl_default_runtime)

ament_package()

