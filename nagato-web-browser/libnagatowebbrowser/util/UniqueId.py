

class NagatoUniqueId(object):

    _id = 0

    def __call__(self):
        NagatoUniqueId._id += 1
        return "unique_id_{}".format(NagatoUniqueId._id)
