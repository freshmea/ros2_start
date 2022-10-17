#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <stdio.h>
#include <unistd.h>
#include <termios.h>

void print_info(void);
int getch(void);

int main(int argc, char **argv)
{
  ros::init(argc, argv, "teleop_turtlesim");
  ros::NodeHandle nh;
  ros::Publisher pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);

  geometry_msgs::Twist tw;
  ros::Rate loop_rate(10);

  int ch = 0, cnt = 0;

  print_info();

  while(ros::ok()) {
  {
    ch = getch();
    
    if     (ch == 'w') { tw.linear.x =  2.0; tw.angular.z =  0.0; cnt++; }
    else if(ch == 's') { tw.linear.x = -2.0; tw.angular.z =  0.0; cnt++; }
    else if(ch == 'a') { tw.linear.x =  0.0; tw.angular.z =  2.0; cnt++; }
    else if(ch == 'd') { tw.linear.x =  0.0; tw.angular.z = -2.0; cnt++; }
    else if(ch == ' ') { tw.linear.x =  0.0; tw.angular.z =  0.0; cnt++; }
    else if(ch == '\x03') break;
    else;

    if(cnt == 10) { cnt = 0; print_info(); }

    pub.publish(tw);

    t.linear.x = t.angular.z = 0.0;
    loop_rate.sleep();
  }
  return 0;
}

void print_info()
{
  puts("Remote Control turtle of turtlesim_node");
  puts("---------------------------------------");
  puts("               (forward)               ");
  puts("                   w                   ");
  puts("  (turn-left) a    s    d (turn-right) ");
  puts("                (back)                 ");
  puts("---------------------------------------");
  puts("### type Ctrl-C to quit                ");
  puts("");
}

int getch(void)
{
  int ch;
  struct termios oldt;
  struct termios newt;

  tcgetattr(STDIN_FILENO, &oldt);
  newt = oldt;

  newt.c_lflag &= ~(ICANON | ECHO);
  newt.c_iflag |= IGNBRK;
  newt.c_iflag &= ~(INLCR  | ICRNL | IXON  | IXOFF);
  newt.c_lflag &= ~(ICANON | ECHO  | ECHOK | ECHOE | ECHONL | ISIG | IEXTEN);
  newt.c_cc[VMIN] = 1;
  newt.c_cc[VTIME] = 0;
  tcsetattr(fileno(stdin), TCSANOW, &newt);

  ch = getchar();

  tcsetattr(STDIN_FILENO, TCSANOW, &oldt);

  return ch;
}