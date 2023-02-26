import pika, json

def upload(f, fs, channel, access):
    # upload file to mongodb using gridfs
    try:
        fid = fs.put(f)
    except Exception as err:
        return "Internal server error", 500

    # store msg in dict
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    # put msg on queue
    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            # serialize dict to json str
            body=json.dumps(message),
            properties=pika.BasicProperties(
                # pod is stateful within k8 cluster
                # so when msgs are added to the q, they need to
                # be persisted, so that if the pod fails,
                # when it spins back up, the msgs are still there
                # i.e. they're persistent
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except:
        # delete file if it isn't successfully added to the q
        fs.delete(fid)
        return "Internal server error", 500