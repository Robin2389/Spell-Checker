// This Program Is Currently In Progress.
// The purpose of this program is to run the same
// Spell Check function that the python program runs.

#include <thread>
#include <ctime>
#include <regex>
#include <iostream>
using namespace std;

void PrintMatches(string str, regex reg) {
  smatch matches;
  cout << boolalpha;
  // Boolalpha because all booleans are usually zero an

  while (regex_search(str, matches, reg)) {
    cout << "Is there a match : " <<
                matches.ready() << "\n";
    cout << "Are there no matches : " <<
                matches.empty() << "\n";
    cout << "Number of matches : " <<
                matches.size() << "\n";
    cout << "Matching Word : " << matches.str(1) << "\n";
                //for loop hear possible to print matches
    str = matches.suffix().str();
    cout << "\n";
  }
}

void PrintMatches2(string str, regex reg) {
  sregex_iterator currentMatch(str.begin(), str.end(), reg);
  sregex_iterator lastMatch;
  while(currentMatch != lastMatch) {
    smatch match = *currentMatch;
    string s = match.str();
    string sl = s;
    transform(sl.begin(), sl.end(), sl.begin(), ::tolower);
    // Call the trie function here,
        // is sl in dictionary.
        // if not, print s
    cout << s << "\n";
    currentMatch++;
  }
  cout << endl;
}


int main()
{
  string str = "This is a test";
  regex reg ("([a-zA-Z]+('s)?)");
  PrintMatches(str, reg);

  string str2 = "Test quote quote /n multiline /n quote ";

  regex reg2 ("([a-zA-Z]+('s)?)");
  PrintMatches2(str2, reg2);
  return 0;
}
