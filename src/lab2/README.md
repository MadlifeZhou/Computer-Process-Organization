# Computer-Process-Organization

HDU-ITMO Computer Process Organization labtoray work

Group Name: **JIDI**

Group Member: 

- **Wang Jiayi**
- **Zhou Guancheng** (ID: 192050193)

## Lab 2

### Variant Description: Variant 1

Our task is to convert a string into a Mathematical expression and calculate the correct output of its mathematical formula. Among them, the user can input the character string of the function defined by himself in the form of f (x), and can calculate the functions of sin, cos, log, pow and other forms, and output the corresponding calculation result.

### Synopsis

The arithmetic expression we usually use is an infix expression, such as 1 + 3 * 2. The characteristic of the infix expression is that the binary operator is always placed between the two arithmetic objects related to it.

It is easier to understand by humans, but it is very troublesome to process by computers. The order of calculation is often determined by the content of the expression, which is irregular

The suffix expression, the characteristic of the suffix expression is: each operator is placed after its operation object, taking the above infix expression 1 + 2 * 3 as an example, the conversion to the suffix expression is 123 * +

Our task is to convert the infix expression into a suffix expression that the computer can process for calculation

### Contribution summary for each group member

Wang Jiayi is responsible for the preparation and design of the main code. Zhou Guancheng is responsible for the debugging and modification of the code and the preparation of the test class.

### Explanation of taken design decisions and analysis

​	**Convert infix expression to suffix expression**

1. Scan the infix expression from left to right 

2. If it is a number, then push it directly into the array num

3. If it is an operand, further judgment is required

   (1) If it is the left parenthesis '(' directly onto the stack opera

   (2) If it is an operator ('+', '-', '*', '/'), first determine the priority of the operand on the top of the stack of the array opera (if it is an empty stack, then push it directly into the array opera ), If it is the left parenthesis, then directly push the stack into the array opera, if the top of the stack is an operator, and the priority of the top operator is greater than the operator

   Then push the operator at the top of the stack onto the stack num and repeat step 3. If the priority of the operator at the top of the stack is less than this operator, then put the operator on the stack directly into opera

   (3) If it is the right parenthesis ')', it means that there must be a left parenthesis in the opera array (if you have not entered a mistake), then the operators in opera will be pushed out of the stack in order and put on the stack. Go to num until you encounter the left bracket '(' (note that the left bracket does not need to be pushed to num)

4. If the infix expression has been scanned, then the operands in opera will be popped out of the stack one by one and put into the stack to num. If there is no scan, repeat steps 1-3

   It should be noted that the closer the operand in opera is to the top of the stack, the higher the priority

   **Suffix expression evaluation**

   After completing the infix expression to suffix expression, the next step is the calculation of the suffix expression. The calculation of the suffix expression is slightly simpler than that of the infix to suffix conversion. It only needs to convert the suffix expression from left to right. Scan one after the other and put them on the stack one by one,

   The circumstances to consider are as follows

   1. If it is a number, then push it directly into the num

   2. If it is an operator, push the two numbers on the top of the stack (because the operators we consider are addition, subtraction, multiplication, and division are all binary operators, only two operands are needed). Digits to perform the corresponding operation, and push the operation result to the stack

   3. Until you encounter `'\0'`

### Work Demonstration

1. Test add 

   ![image-20200518191711126](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtjbj7u7j30g003a3yy.jpg)

   ![image-20200518191909271](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtl9r1yij30iw05pq57.jpg)

2. Test sub function

   ![image-20200518191759381](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtk416jwj30fp036jro.jpg)

   ![image-20200518191931890](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtlntttcj30j8073dil.jpg)

3. Test multiplication

   ![image-20200518192128635](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtnoybyyj30id03f3z4.jpg)

<img src="https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtoayck7j30j70700tj.jpg" alt="image-20200518192159973"  />

4. Test division

![image-20200518192532676](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtrx38ynj30gc02p0t3.jpg)

![image-20200518192552992](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewts9oqv1j30ix076q5p.jpg)

5. Test mixed string

   ![image-20200518192635970](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtt1s9k1j30iz04it98.jpg)

![image-20200518192657717](https://tva1.sinaimg.cn/large/007S8ZIlgy1gewtte3czzj30j5076dim.jpg)

### Conclusion

In this experiment we completed the function of inputting a string and calculating the result of the expression of the string operation. We can handle custom functions, sin functions, cos functions, and operate with operators such as addition, subtraction, multiplication and division. We converted the infix expression into a suffix expression, processed it in the suffix expression, and calculated its result correctly