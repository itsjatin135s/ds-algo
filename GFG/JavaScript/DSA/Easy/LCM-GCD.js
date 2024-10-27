function lcmAndGcd(a, b) {
  //code here
  A = a;
  B = b;
  while (a > 0 && b > 0) {
    if (a > b) a = a % b;
    else b = b % a;
  }
  let gcd = a > 0 ? a : b;

  let lcm = (A * B) / gcd;
  return [lcm, gcd];
}

console.log(lcmAndGcd(6, 10));
