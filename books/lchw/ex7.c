#include <stdio.h>

int main (int argc, char *argv[]) {
    int bugs = 100;
    double bug_rate = 1.2;

    printf("You have %d bugs at the rate of %f.\n", bugs, bug_rate);

    long universe_of_defects = 1L * 1024L * 1024L * 1024L * 1024 * 1024;
    printf("The entire universe has %ld bugs.\n", universe_of_defects);

    double expcted_bugs = bugs * bug_rate;
    printf("YOu are expected to have %f bugs.\n", expcted_bugs);

    double part_of_universe = expcted_bugs / universe_of_defects;
    printf("This is only a %e portion of the universe\n", part_of_universe);

    char nul_byte = '\0';
    printf("Char: %c\n", nul_byte);
    int care_percentage = bugs * nul_byte;
    printf("Which means you should care %d%%.\n", care_percentage);

    return 0;
}