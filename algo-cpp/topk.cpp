// please complete the class definition
#include <vector>
#include <string>
#include <iostream>
#include <map>

class TopK {
private:
    // Hashtable with words and their frequencies.
    std::map<std::string, int> word_freq;
  
    // Max size of the returned vector.
    size_t k;

public:
    /*
     * Initialize if needed.
     */
    TopK(size_t k_) {
      // Save k.
      k = k_;
    }
    /*
     * Record a new word in the data stream.
     */
    void add(const std::string& word) {
      try {
        word_freq[word] = word_freq[word] +1;
      } catch (std::exception e) {
        word_freq.insert( std::pair<std::string, int> (word, 1));
      }//: catch
      
    }
    /*
     * @return: the current top k frequent words, sorted by frequency.
     */
    std::vector<std::string> topk() {
      std::vector<std::string> ret_words;
      // Edge case 0: do not have enough elements.
      if (word_freq.size() <= k) {
        // We will simply return what we got.
        for (auto it = word_freq.begin(); it != word_freq.end(); it++)
          ret_words.push_back(it->first);
        return ret_words;
      }//: if
        
  
      // While the retured list is smaller then required.
      while (ret_words.size() < k) {
        int biggest_freq = -1;
        std::map<std::string, int>::iterator biggest_it;

        // Try to find the biggest element there.
        for (auto it = word_freq.begin(); it != word_freq.end(); it++) {
          if (it->second > biggest_freq){
            biggest_it = it;
            biggest_freq = it->second;
          }//: if
        }//: for
        // We are sure that biggest_it is pointing at "something".
        ret_words.push_back(biggest_it->first);
        // Remove that element from the hashtable.
        word_freq.erase(biggest_it);
      }//: while
      // Return k elements.
      return ret_words;
      
    }
};

// testing code
int main() {
  TopK kk(2);
  // First add all the words.
  kk.add("car");
  kk.add("toy");
  kk.add("car");
  kk.add("toy");
  kk.add("car");
  kk.add("fun");

  // Query for the top K words.
  std::vector<std::string> res = kk.topk();
  for (const auto& w : res) {
    std::cout << w << std::endl;
  }
  return 0;
}
