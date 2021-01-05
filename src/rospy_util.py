import time
import rospy
import rosservice
import rostopic


class PublisherWithConnection(rospy.Publisher):

    def __init__(self, *args, num_connections=1, retry_sec=0.1, timeout=1, **kwargs):
        super().__init__(*args, **kwargs)
        self._wait_for_connection(num_connections, retry_sec, timeout)

    def _wait_for_connection(self, num_connections, retry_sec, timeout):
        start = time.time()
        while not rospy.is_shutdown():
            rospy.sleep(retry_sec)
            if self.get_num_connections() >= num_connections:
                return
            if time.time() - start > timeout:
                rospy.logwarn('wait_for_connection timeout: {}'.format(self.name))
                return


class PublisherAutoTyped(rospy.Publisher):

    def __init__(self, name, data_class=None, *args, **kwargs):
        if not data_class:
            resolved_name = rospy.names.resolve_name(name)
            data_class, _, _ = rostopic.get_topic_class(resolved_name)
        super().__init__(name, data_class, *args, **kwargs)


class ServiceProxyAutoTyped(rospy.ServiceProxy):

    def __init__(self, name, service_class=None, *args, **kwargs):
        if not service_class:
            resolved_name = rospy.names.resolve_name(name)
            service_class = rosservice.get_service_class_by_name(resolved_name)
        super().__init__(name, service_class, *args, **kwargs)
