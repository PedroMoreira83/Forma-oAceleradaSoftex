class Fibonacci {
  static fibo(n) {
    if (n < 4) {
      return n;
    } else {
      return this.fibo(n - 2) + this.fibo(n - 4);
    }
  }
}
