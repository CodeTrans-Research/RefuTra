int f_gold ( int a, int b ) {
  if (a == 0 || b == 0) return 1;
  return (int)std::floor(std::log10(std::abs(a)) + std::log10(std::abs(b))) + 1;
}