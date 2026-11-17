
set_nums = {1,2,4,5,3,8,7,6}

num_sum = sum(set_nums)

div_sum = len(set_nums)

num_remainder = num_sum/div_sum

print('This is the average total of your set of numbers:',set_nums,'=',str(num_sum)+'/'+str(div_sum),'=',(num_remainder))

print('This is the average total of your set of numbers: {} = {}/{} = {}'.format(set_nums,str(num_sum),str(div_sum),num_remainder))

print(f'This is the average total of your set of numbers: {set_nums} = {num_sum}/{div_sum} = {num_remainder}')
