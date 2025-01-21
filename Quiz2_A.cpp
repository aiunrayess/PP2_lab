#include <iostream>
int main()
{
    int amount_of_enemies = 0;
    std::cin >> amount_of_enemies;
    int a[100];
    for (int i = 0; i < amount_of_enemies; ++i)
    {
        std::cin >> a[i];
    }
    int right_hand_sum = 0;
    int left_hand_sum = 0;
    int righ_hand_count_odd_number = 0;
    int left_hand_count_even_number = 0;
    for (int i = 0; i < amount_of_enemies; ++i)
    {
        if (a[i] % 2 == 0)
        {
            left_hand_sum += a[i];
            ++left_hand_count_even_number;
        }
        else
        {
            right_hand_sum += a[i];
            ++righ_hand_count_odd_number;
        }
    }
    std::cout << "Left hand magic power: " << left_hand_count_even_number * left_hand_sum << '\n'
              << "Right hand magic power: " << righ_hand_count_odd_number * right_hand_sum;
}