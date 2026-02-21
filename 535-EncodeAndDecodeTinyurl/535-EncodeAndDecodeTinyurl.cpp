// Last updated: 2/21/2026, 9:43:46 AM
class Solution {
public:

    // Encodes a URL to a shortened URL.
    unordered_map<string,string> short_DB,long_DB;
    string getcode()
    {
        string code="";
        string s="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        for(int i=0;i<6;i++)
        {
            code+=s[rand()%62];
        }
        return "http://tinyurl.com/"+code;
    }
    string encode(string longUrl) {
        if(long_DB.find(longUrl)!=long_DB.end())
        {
            return long_DB[longUrl];
        }
        string code=getcode();
        while(short_DB.find(code)!=short_DB.end())
        {
            code=getcode();
        }
        long_DB[longUrl]=code;
        short_DB[code]=longUrl;
        return code;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        
        return short_DB[shortUrl];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));