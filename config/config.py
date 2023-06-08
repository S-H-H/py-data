


import os
import configparser

# os.chdir("G:\dataProcess\dataProcess\interface_post")
# os.chdir("/")
os.chdir(os.getcwd())

# configparser读取.ini文件不区分大小
class OperationalError(Exception):
    """operation error."""


class Dictionary(dict):
    """ custom dict."""

    def __getattr__(self, key):
        return self.get(key, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class Config:

    def __init__(self, file_name="conf.ini", cfg=None):
        config = configparser.ConfigParser()
        config.read(file_name, encoding='utf-8')
        for section in config.sections(): # sections() 得到所有的section，以列表形式返回

            setattr(self, section, Dictionary()) #self.section = Dictionary()
            for name, raw_value in config.items(section): # items 得到section的所有键值对
                # print(name + " = " + raw_value)
                try:
                    # Ugly fix to avoid '0' and '1' to be parsed as a
                    # boolean value.
                    # We raise an exception to goto fail^w parse it
                    # as integer.
                    if config.get(section, name) in ["0", "1"]: # get(section,option) 得到section中的option值，返回string/int类型的结果
                        print("***")
                        raise ValueError

                    # value = config.getboolean(section, name) #会将整数05中的0去掉
                    value = config.get(section, name)
                except ValueError:
                    try:
                        value = config.getint(section, name)
                    except ValueError:
                        value = config.get(section, name)
                setattr(getattr(self, section), name, value) #getattr(self, section) 获得对象属性self.section的值

    def get(self, section):
        """Get option.
        @param section: section to fetch.
        @return: option value.
        """
        try:
            return getattr(self, section)
        except AttributeError as e:
            raise OperationalError("Option %s is not found in configuration, error: %s" %(section, e))

if __name__ == '__main__':
    conf = Config()
    # file_data = conf.get("bossForwardApi")
    # print(file_data)
    # print(file_data)
    # print(file_data.input_file)#大写默认转换位小写
    # print(file_data.output_file)

    dir = os.chdir(os.getcwd()) #
    print(os.getcwd())
