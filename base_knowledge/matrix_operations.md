<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

#向量运算

#一、向量间的运算
	两个相同维数的向量X和y的 **点积** 可看作矩阵乘积。

###(1)交换律： \\( x^{\rm T}y = y^{\rm T}x \\)
###$$因为 \qquad x^{\rm T}y=(x^{\rm T}y)^{\rm T}=y^{\rm T}x$$

#二、向量与矩阵的运算
	x是向量,A是矩阵。
###几个基本的雅可比矩阵：\\( \nabla Ax=A,特别地，\nabla x=I\\)
###向量内积的求导法则： \\( \nabla (a^{\rm T})x=a \\)
###\\( \nabla ||x||^2= \nabla (x^{\rm T}x)=2x \\)
### \\( x^{\rm T}A =A^{\rm T}x \Longrightarrow \nabla (x^{\rm T}Ax)=(A+A^{\rm T})x \\)
###向量内积求导法则：\\( \nabla (u^{\rm T}v)=(\nabla u)^{\rm T}v+( \nabla v)^{\rm T}u\\)

#三、矩阵的加减法
### 交换律：A + B = B + A
### 结合律：(A + B）+C = A + （B + C）

#四、矩阵与数的乘法
### 结合律：   \\((\lambda \mu)A = \lambda (\mu A); (\lambda + \mu)A = \lambda A +\mu A\\)
### 分配率： \\( \lambda(A+B)=\lambda A+\lambda B \\)

#五、矩阵与矩阵的乘法
###结合律： \\( (AB)C = A(BC)\\)
###分配率： \\(A(B\pm C) = AB\pm AC   \qquad  (B \pm C)A = BA\pm CA\\)
### \\( \qquad \qquad(\lambda A )B = \lambda(AB) = A(\lambda B)\\)

#六、矩阵的转置
###  \\( A{\rm '} =A^{\rm T} \\)
###  \\((A{\rm '}){\rm '}= A \\)
### \\((A + B){\rm '} = A{\rm '} + B {\rm '} \\)
### \\((AB){\rm '} = B{\rm '}A{\rm'} \\)
### \\((\lambda A){\rm '} = \lambda A{\rm '}\\)

#七、矩阵的逆
	定义：如果  **AB = BA = E** 则说矩阵A是 **可逆** 的，并把矩阵B称为A的一个逆矩阵。记作： \\( A^{-1} $$\\)
###定理：矩阵A可逆的充分必要条件是 \\(|A|\neq 0\\) , 且 \\(A^{-1}=\frac{1}{A} A^{*} \\) ,其中 \\(A^{\rm *} \\) 为矩阵A的伴随矩阵。

###(1)若A可逆，则 \\(A^{-1}\\) 亦可逆，且\\((A^{-1})^{-1} = A\\)
###(2)若A可逆，数\\(\lambda \neq 0 \\),则\\(\lambda A\\)可逆，且\\((\lambda A)^{-1}=\frac{1}{\lambda}A^{-1}\\)
###(3)若A,B为同阶方阵且可逆，则AB亦可逆，且 \\((AB)^{-1}=B^{-1}A^{-1}\\)
###(4)若A可逆，则\\(A^{\rm T}\\)亦可逆，且\\( (A^{\rm T})^{-1}=(A^{-1}){\rm T} \\)
###(5)若A可逆，则有\\(|A^{-1}|=|A|^{-1}\\)

#八、奇异矩阵与非奇异矩阵
##定义： 当|A|=0 时，A称为奇异矩阵，当\\(|A| \neq 0\\) 时，称为非奇异矩阵。
  由此可知A时可逆矩阵的充要条件时A为非奇异矩阵。

#参考

-[矩阵运算]（）

