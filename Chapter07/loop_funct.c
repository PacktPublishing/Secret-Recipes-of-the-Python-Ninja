double add(double x, double y)
{
  return x + y;
}

int main(void)
{
  int i = 0;
  double x = 0;
  while (i < 1000000000) {
    x += 1.0;
    add(x, x);
    i++;
  }
    return 0;
}
