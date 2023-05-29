import time
import pytest
class Test01:
    age = 16

    def test_01_luban(self):
        #time.sleep(3)
        print("测试01")

    @pytest.mark.run(order=3)
    def test_02_luban(self):
        #time.sleep(3)
        print("测试02")
    @pytest.mark.hellotest
    @pytest.mark.skip(reason="不想测")
    @pytest.mark.run(order=1)
    def test_03_luban(self):
        #time.sleep(3)
        print("测试03")

    def test_04_luban(self):
        #time.sleep(3)
        print("测试04")

    @pytest.mark.zeng
    @pytest.mark.run(order=2)
    @pytest.mark.skipif(age<18,reason="太小了")
    def test_05_luban(self):
        #time.sleep(3)
        print("测试05")
        
    