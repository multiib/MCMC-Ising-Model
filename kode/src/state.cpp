#include "state.hpp"
#include <armadillo>
#include <random>
#include <chrono>



//konstruktør
State::State(int size, double temp, int seed){
  L = size;
  T = temp;

  //pdf
 uniform_dist = std::uniform_int_distribution<int>(1, L);
  uniform_real = std::uniform_real_distribution<> (0, 1);
  generator.seed(seed);

  //tilstandsmatrise
  int N = L*L;
  S = arma::mat(L+2, L+2);
  S = arma::sign(S.randu()-0.4);
  S.replace(0, 1);

  //periodisitet
  make_periodic();
}

void State::make_periodic()
  {
    //kopierar rendene til tilstanden for å forsikre periodisitet

  arma::vec p_right = S.col(1);
  arma::vec p_left = S.col(L);
  S.col(0) = p_left;
  S.col(L+1) = p_right;
 arma::rowvec p_top = S.row(1);
  arma::rowvec p_bottom = S.row(L);
  S.row(0) = p_bottom;
  S.row(L+1) = p_top;
  //lettare å visualisere
  S(0, 0) = 0;
   S(L+1, L+1) = 0;
   S(L+1, 0) = 0;
   S(0, L+1) = 0;
}


//flippar ein spinn
void State::flip_random_spinn()
{
  //std::cout << "Calling flip spinn" << std::endl;

  //brukar generatoren til å velge ein tilfeldig spinn
  int index_1  = uniform_dist(generator); // korleis kalle på arma-element med ein index?
  int index_2  = uniform_dist(generator);
  //std::cout << "Indeksar: " << index_1  << ", " << index_2 << std::endl;

  //energiforskjel om spinnen flippast
   double energy_diff = delta_E(index_1, index_2);
   double rel_prob = std::exp(-energy_diff/T); //double check this!

   //godkjenningssannsyn
   double A = std::min(1.,  rel_prob);
   //std::cout << A << std::endl;
   //aksepter eller avvis tilstanden
   double r = uniform_real(generator);
   //std::cout<< "r: " << r << std::endl;
   if (r <= A){
     std::cout << "Flipping!" << std::endl;
     S(index_1, index_2) = -S(index_1, index_2); //flip the spin!
     make_periodic();
   }
}


//rekn ut energidifferanse
double State::delta_E(int &index_1, int &index_2)
{
  //std::cout << "Calculate energy difference" <<std::endl;
  double D_inter_E = 0;
  D_inter_E += S(index_1, index_2)*S(index_1+1, index_2);
  D_inter_E += S(index_1, index_2)*S(index_1-1, index_2);
   D_inter_E += S(index_1, index_2)*S(index_1, index_2+1);
   D_inter_E += S(index_1, index_2)*S(index_1, index_2-1);
   D_inter_E = 2*D_inter_E;

  return D_inter_E;
}
