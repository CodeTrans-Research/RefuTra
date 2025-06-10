std::string f_gold(double num, int k_prec) {
    std::string binary = "";
    int Integral = (int) num;
    double fractional = num - Integral;
    while (Integral > 0) {
        int rem = Integral % 2;
        binary += (char) (rem + '0');
        Integral /= 2;
    }
    std::reverse(binary.begin(), binary.end());
    binary += ('.');
    while (k_prec-- > 0) {
        fractional *= 2;
        int fract_bit = (int) fractional;
        if (fract_bit == 1) {
            fractional -= fract_bit;
            binary += (char) (1 + '0');
        }
        else {
            binary += (char) (0 + '0');
        }
    }
    return binary;
}