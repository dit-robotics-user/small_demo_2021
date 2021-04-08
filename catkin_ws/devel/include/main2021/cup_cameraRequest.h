// Generated by gencpp from file main2021/cup_cameraRequest.msg
// DO NOT EDIT!


#ifndef MAIN2021_MESSAGE_CUP_CAMERAREQUEST_H
#define MAIN2021_MESSAGE_CUP_CAMERAREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace main2021
{
template <class ContainerAllocator>
struct cup_cameraRequest_
{
  typedef cup_cameraRequest_<ContainerAllocator> Type;

  cup_cameraRequest_()
    : req(false)  {
    }
  cup_cameraRequest_(const ContainerAllocator& _alloc)
    : req(false)  {
  (void)_alloc;
    }



   typedef uint8_t _req_type;
  _req_type req;





  typedef boost::shared_ptr< ::main2021::cup_cameraRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::main2021::cup_cameraRequest_<ContainerAllocator> const> ConstPtr;

}; // struct cup_cameraRequest_

typedef ::main2021::cup_cameraRequest_<std::allocator<void> > cup_cameraRequest;

typedef boost::shared_ptr< ::main2021::cup_cameraRequest > cup_cameraRequestPtr;
typedef boost::shared_ptr< ::main2021::cup_cameraRequest const> cup_cameraRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::main2021::cup_cameraRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::main2021::cup_cameraRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::main2021::cup_cameraRequest_<ContainerAllocator1> & lhs, const ::main2021::cup_cameraRequest_<ContainerAllocator2> & rhs)
{
  return lhs.req == rhs.req;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::main2021::cup_cameraRequest_<ContainerAllocator1> & lhs, const ::main2021::cup_cameraRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace main2021

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::main2021::cup_cameraRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::main2021::cup_cameraRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::main2021::cup_cameraRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::main2021::cup_cameraRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::main2021::cup_cameraRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::main2021::cup_cameraRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::main2021::cup_cameraRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "be3c44e19d0c6b00b25e356c69155e2a";
  }

  static const char* value(const ::main2021::cup_cameraRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbe3c44e19d0c6b00ULL;
  static const uint64_t static_value2 = 0xb25e356c69155e2aULL;
};

template<class ContainerAllocator>
struct DataType< ::main2021::cup_cameraRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "main2021/cup_cameraRequest";
  }

  static const char* value(const ::main2021::cup_cameraRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::main2021::cup_cameraRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool req\n"
;
  }

  static const char* value(const ::main2021::cup_cameraRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::main2021::cup_cameraRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.req);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct cup_cameraRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::main2021::cup_cameraRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::main2021::cup_cameraRequest_<ContainerAllocator>& v)
  {
    s << indent << "req: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.req);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MAIN2021_MESSAGE_CUP_CAMERAREQUEST_H