# rospy_util

## Usage

### PublisherWithConnection

```python
pub = rospy_util.PublisherWithConnection('/topic_name', DataClass, num_connections=1)
```

### PublisherAutoTyped

```python
# Instead of rospy.Publisher('/topic_name', DataClass)
pub = rospy_util.PublisherAutoTyped('/topic_name')
```

### ServiceProxyAutoTyped

```python
# Instead of rospy.ServiceProxy('/service_name', ServiceType)
svc = rospy_util.ServiceProxyAutoTyped('/service_name')
```
