#include "ros/ros.h"
#include "rosbag/bag.h"
#include "rosbag/view.h"
#include "std_msgs/String.h"

/* 
 * 将两个bag包合并成一个新的bag包
*/

int main(int argc, char** argv) {
    // 初始化ROS节点
    ros::init(argc, argv, "bag_merger");
    ros::NodeHandle nh;

    int radar_count = 0;
    int lidar_count = 0;

    double timestamp_temp = 0;

    // 从ROS参数服务器获取输入bag文件的路径和输出bag文件的路径
    std::string bag1_path, bag2_path, output_bag_path;
    bag1_path = "/home/dearmoon/datasets/NWU/日雪不颠簸高速/4DRadar/xr.bag";
    bag2_path = "/home/dearmoon/datasets/NWU/日雪不颠簸高速/bdbxr.bag";
    output_bag_path = "/home/dearmoon/datasets/NWU/日雪不颠簸高速/radar_lidar.bag";

    // nh.param<std::string>("bag1_path", bag1_path, "/home/dearmoon/datasets/NWU/日晴不颠簸低速3/4DRadar/RiQingBuDianBoDiSu3.bag");   // Radar
    // nh.param<std::string>("bag2_path", bag2_path, "/home/dearmoon/datasets/NWU/日晴不颠簸低速3/3.bag");                             // IMU
    // nh.param<std::string>("output_bag_path", output_bag_path, "/home/dearmoon/datasets/NWU/日晴不颠簸低速3/imu_4DRadar.bag");

    // 打开输入bag文件和输出bag文件
    rosbag::Bag bag1(bag1_path, rosbag::bagmode::Read);
    std::cout << "bag1_path: " << bag1_path << std::endl;

    rosbag::Bag bag2(bag2_path, rosbag::bagmode::Read);
    std::cout << "bag2_path: " << bag2_path << std::endl;

    rosbag::Bag output_bag(output_bag_path, rosbag::bagmode::Write);
    std::cout << "output_bag_path: " << output_bag_path << std::endl;

    // 创建一个Topic过滤器，选择需要保留的所有话题
    // rosbag::View view1(bag1, rosbag::TopicQuery("/a1") || rosbag::TopicQuery("/a2") || rosbag::TopicQuery("/a3"));
    // rosbag::View view2(bag2, rosbag::TopicQuery("/b1") || rosbag::TopicQuery("/b2"));
    rosbag::View view1(bag1, rosbag::TopicQuery("/ars548_process/detection_point_cloud"));
    rosbag::View view2(bag2, rosbag::TopicQuery("/livox/lidar") );

    // 循环读取输入bag文件中的消息并写入输出bag文件
    for (const rosbag::MessageInstance& msg : view1) {
        output_bag.write(msg.getTopic(), msg.getTime(), msg);
        radar_count++;
    }

    for (const rosbag::MessageInstance& msg : view2) {
        // std::cout << " msg.getTime(): " << msg.getTime() << std::endl;
        lidar_count++;
        output_bag.write(msg.getTopic(), msg.getTime(), msg);


        // 检查时间戳顺序是否正确
        if(lidar_count == 1){
            timestamp_temp = msg.getTime().toSec();
        }
        else if( timestamp_temp > msg.getTime().toSec())  {
            std::cout << "timestamp is in disorder!!!" << std::endl; 
            exit(1);
        }  
        else {
            timestamp_temp = msg.getTime().toSec();
            std::cout << "timestamp "<< timestamp_temp <<  " is in order" << std::endl;
        }

    }

    std::cout << "radar_count: " << radar_count << std::endl;
    std::cout << "lidar_count: " << lidar_count << std::endl;

    // 关闭输入和输出的bag文件
    bag1.close();
    bag2.close();
    output_bag.close();

    // 进入ROS事件循环，接收和处理ROS消息
    ros::spin();

    return 0;
}
