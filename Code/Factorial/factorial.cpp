#include <iostream>
using namespace std;

void factorial()
{
  cout << "Enter your number: ";

  int input_number;
  cin >> input_number;

  int inital_value = input_number;
  int factorial = 1;
  while (input_number > 0)
  {
    factorial *= input_number;
    input_number--;
  }

  cout << "The factorial of " << inital_value << " is " << factorial << endl;
}

int main()
{
  factorial();
  return 0;
}