assert 1==1
try:
    assert 2==1 
except:
    print('test case didnt pass')
finally:
    print('test case passed , finally block ')