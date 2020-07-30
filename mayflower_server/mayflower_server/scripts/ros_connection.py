from ..controls.ros_publish import RosControlsPublisher



def init_client(host=None, topic=None):
    if host and topic:
        return RosControlsPublisher(host, topic)

    if host:
        return RosControlsPublisher(ros_host=host)

    if topic:
        return RosControlsPublisher(topic=topic)

    return RosControlsPublisher()
