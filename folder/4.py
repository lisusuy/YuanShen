import os
import pickle


def execute_os_command():
    command = "echo 'os command'"
    result = os.system(command)
    print(f"Result of executing OS command: {result}")


def deserialize_pickle_data():
    serialized_data = b'\x80\x03X\x0b\x00\x00\x00Hello, World!q\x00.'
    obj = pickle.loads(serialized_data)
    print(f"Deserialized object: {obj}")

if __name__ == "__main__":
    execute_os_command()
    deserialize_pickle_data()