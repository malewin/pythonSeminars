import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())

robot_list = []
human_list = []
data_list = list(data['whoAmI'])
for i in range(len(data_list)):
    if data_list[i] == 'robot':
        robot_list.append(1)
        human_list.append(0)
    else:
        robot_list.append(0)
        human_list.append(1)
result_robot = pd.DataFrame({'robot': robot_list})
result_human = pd.DataFrame({'human': human_list})
df = result_robot.join(result_human)
print(df)

# print(robot_list)
# print(human_list)
# print(result_robot)
# print(result_human)
# df = pd.concat([result_robot, result_human])
# print(df)

# data_list = list(data['whoAmI'])
# for i in range(len(data_list)):
#     if data_list[i] == 'robot':
#         data_list[i] = 0
#     else:
#         data_list[i] = 1
# result = pd.DataFrame({'whoAmI': data_list})
# print(data_list)
# print(result)
