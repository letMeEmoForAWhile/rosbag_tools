#include <ros/ros.h>
#include <std_msgs/String.h>

int main(int argc, char** argv) {
    ros::init(argc, argv, "command_sender");
    ros::NodeHandle nh;

    ros::Publisher command_pub = nh.advertise<std_msgs::String>("/command", 10);

    // 创建一个命令消息
    std_msgs::String command_msg;
    command_msg.data = "output_aftmapped";  // 可以在这里更改为 "time", "point_distribution" 或 "output_aftmapped"

    // 设置发布频率
    ros::Rate loop_rate(60);  // Hz

    while (ros::ok()) {
        // 发布命令
        command_pub.publish(command_msg);
        ROS_INFO("Published command: %s", command_msg.data.c_str());

        ros::spinOnce();
        loop_rate.sleep();  // 控制发送频率
    }

    return 0;
}
