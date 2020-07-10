# - * - coding: utf-8 - * -
import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.set('name', 'maple')
print(r.get('name'))


class RedisHelper(object):
      def __init__(self):
           self.__conn = redis.Redis(host='127.0.0.1', port=6379)  # 连接 Redis
           self.channel = "monitor"  # 定义名称

      def publish(self, msg):  # 定义发布方法
           self.__conn.publish(self.channel, msg)
           return True

      def subscribe(self):  # 定义订阅方法
           pub = self.__conn.pubsub()
           pub.subscribe(self.channel)
           pub.parse_response()
           return pub




def expire_test():
    # 这个 Redis 连接不能用，请根据自己的需要修改
    r = redis.Redis(host ="127.0.0.1", port = 6379)
    r.set("2", "4028b2883d3f5a8b013d57228d760a93")
    # 如果成功就返回 True，如果失败就返回 False，下面的 20 表示 20s
    print(r.expire("2",20))
    # 如果没有过期我们能得到键 2 的值；否则，返回 None
    print(r.get("2"))
    r.set("2", "4028b2883d3f5a8b013d57228d760a93")
    # 成功就返回 True 失败就返回 False，下面的 1598033936 表示在 2020-08-22 02:18:56 键 2 过期
    print(r.expireat("2",1598033936))
    print(r.get("2"))


def persist_test():
    import redis
    # 这个 Redis 连接不能用，请根据自己的需要修改
    r = redis.Redis(host="127.0.0.1", port=6379)
    print(r.set("111", "11"))
    print(r.set("122", "12"))
    print(r.set("113", "13"))
    print(r.keys(pattern = "11*"))
    # 输出的结果是 [』111『， 』112『]，因为键 122 和 11*不匹配
    r.move(2, 1)
    # 将键 2 移动到数据库 1 中去
    # 设定键 1 的值为 11
    print(r.set("1", "11"))
    # 设定键 1 的过期时间为 100s
    print(r.expire(1, 100))
    # 查看键 1 的过期时间还剩下多少
    print(r.ttl("1"))
    # 目的是 13s 后移除键 1 的过期时间
    import time
    time.sleep(3)
    # 查看键 1 的过期时间还剩下多少
    print(r.ttl("1"))
    # 移除键 1 的过期时间
    r.persist(1)
    # 查看键 1 的过期时间还剩下多少，输出的结果是 None，可以通过 redis desktop manager 查看键 1 的过期时间
    print(r.ttl("1"))

expire_test()
persist_test()

# 发布者
obj_pub = RedisHelper()
obj_pub.publish('hello')

# 订阅者
obj_sub = RedisHelper()
redis_sub = obj_sub.subscribe()

while True:
    msg = redis_sub.parse_response()
    print(msg)