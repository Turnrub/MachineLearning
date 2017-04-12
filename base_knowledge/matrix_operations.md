<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
# 一、矩阵的加减法
## 1、运算性质（假设运算可行）
    满足交换律与结合律
    
### 交换律：   A + B = B + A
### 结合律：  （A + B）+C = A + （B + C）

# 二、矩阵与数的乘法
### 结合律：   $$ (\lambda \mu)A = \lambda (\mu A); (\lambda + \mu)A = \lambda A +\mu A $$
### 分配率：   $$ \lambda(A+B)=\lambda A+\lambda B $$

#三、矩阵与矩阵的乘法
###结合律： $$ (AB)C = A(BC)$$
###分配率： $$ A(B\pm C) = AB\pm AC $$ $$(B \pm C)A = BA\pm CA$$

### $$(\lambda A )B = \lambda(AB) = A(\lambda B)$$

#四、矩阵的转置
$$ A{\rm '} =A^{\rm T} $$
### (1) $$(A{\rm '}){\rm '}= A $$
### (2) $$(A + B){\rm '} = A{\rm '} + B {\rm '} $$
### (3) $$(AB){\rm '} = B{\rm '}A{\rm'} $$
### (4) $$(\lambda A){\rm '} = \lambda A{\rm '}$$

#五、矩阵的逆
##定义：
	如果  **AB = BA = E** 则说矩阵A是 **可逆** 的，并把矩阵B称为A的一个逆矩阵。记作： 
$$ A^{-1} $$
##定理1 矩阵A可逆的充分必要条件是$$|A|\neq 0$$ , 且 $$A^{-1}=\frac{1}{A} A^{*} $$ ,其中 $$A^{\rm *}$$ 为矩阵A的伴随矩阵。
## 逆矩阵的运算性质
###（1）若A可逆，则 $$A^{-1}$$ 亦可逆，且$$(A^{-1})^{-1} = A $$
###(2)若A可逆，数$$\lambda \neq 0 $$,则$$\lambda A$$可逆，且$$(\lambda A)^{-1}=\frac{1}{\lambda}A^{-1}$$
###(3)若A,B为同阶方阵且可逆，则AB亦可逆，且 $$(AB)^{-1}=B^{-1}A^{-1}$$
###(4)若A可逆，则$$A^{\rm T}$$亦可逆，且$$(A^{\rm T})^{-1}=(A^{-1}){\rm T} $$
###(5)若A可逆，则有$$|A^{-1}|=|A|^{-1}$$
#六、奇异矩阵与非奇异矩阵
##定义： 当|A|=0 时，A称为奇异矩阵，当$$|A| \neq 0$$ 时，称为非奇异矩阵。
	由此可知A时可逆矩阵的充要条件时A为非奇异矩阵。

#六、向量间的运算
	两个相同维数的向量X和y的 **点积** 可看作矩阵乘积
 $$ x^{\rm T}y $$

###(1)交换律： $$ x^{\rm T}y = y^{\rm T}x $$
$$x^{\rm T}y=(x^{\rm T}y)^{\rm T}=y^{\rm T}x$$
