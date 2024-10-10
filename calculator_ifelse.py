{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "specify the operator:\n",
      "\n",
      "1=Addition\n",
      "2=substraction\n",
      "3=multiplication\n",
      "4=division\n",
      "\n",
      "30.0\n"
     ]
    }
   ],
   "source": [
    "#simple desktop calculator\n",
    "a=float(input(\"Enter first no:\"))\n",
    "b=float(input(\"enter second no:\"))\n",
    "print('specify the operator:')\n",
    "print(\"\"\"\n",
    "1=Addition\n",
    "2=substraction\n",
    "3=multiplication\n",
    "4=division\n",
    "\"\"\")\n",
    "oper=int(input(\"Enter operator:\"))\n",
    "#addition\n",
    "if oper==1:\n",
    "    s=a+b\n",
    "    print(s)\n",
    "elif oper==2:\n",
    "    sub=a-b\n",
    "    print(sub)\n",
    "elif oper==3:\n",
    "    mult=a*b\n",
    "    print(mult)\n",
    "elif oper==4:\n",
    "    divs=a/b\n",
    "    print(divs)\n",
    "else:\n",
    "    print(\"Error\")                \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
