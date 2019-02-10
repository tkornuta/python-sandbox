#include <iostream>
#include <random>

using namespace std;

#define BINS 20 

int main()
{
     const int nrolls=10000;  // number of experiments
     const int nstars=100;    // maximum number of stars to distribute

     std::default_random_engine generator;
     // Number of failures r that - when reached - will break the experiment.
     int r = 4;
     // Propability of success and failure.
     double p_fail = 1.0/3.0;
     double p_succ = 1.0 - p_fail;

     // This will return the number of successes in a sequence of independent and identically distributed Bernoulli trials 
     // before a specified (non-random) number of failures (denoted r) occurs
     std::negative_binomial_distribution<int> distribution(r, p_succ);

     int p[BINS]={};

     for (int i=0; i<nrolls; ++i) {
         double number = distribution(generator);
         if ((number>=0.0)&&(number<BINS)) ++p[int(number)];
     }

     std::cout << "negative_binomial_distribution (" << r << "," << p_succ << "):" << std::endl;

     for (int i=0; i<BINS; ++i) {
          if (i<9) cout << "  ";
          else if (i == 9) cout << " ";

          std::cout << i << "-" << (i+1) << ": ";
          std::cout << std::string(p[i]*nstars/nrolls,'*') << "   (" << (double)p[i]/nrolls << ")\n";
     }

     return 0;
}