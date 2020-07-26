import os,sys
sys.path.append(os.getcwd())
from nth_carolprime import fun_nth_carolprime
import pytest


@pytest.mark.parametrize('a, result',[
   (0, 7),(1, 47),(2, 223),(3,3967 ),
(4,16127),(5, 1046527), (6, 16769023)

])
def test_fun_nth_carolprime(a, result):
    assert fun_nth_carolprime(a) == result

