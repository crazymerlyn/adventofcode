#include <bits/stdc++.h>
using namespace std;

using pi = pair<int, int>;
constexpr int n=81, m=81, total=n*m;

int dist[6561];

struct Coord {
    int c;
    Coord(): c(0){}
    Coord(int x) :c(x) {}
    Coord left() {return c % m ? Coord{c-1}: Coord{-1};}
    Coord right() {return c % m != m - 1 ? Coord{c+1} : Coord{-1};}
    Coord up() {return Coord{c-m};}
    Coord down() {return Coord{c+m};}
    void operator=(int x) {c=x;}
    operator int() {
        return c;
    }
    bool operator< (const Coord &other) {return c < other.c;}
    bool operator< (const int &other) {return c < other;}
};

bool operator<(const Coord &a, const Coord &b) {return a.c < b.c;}

vector<int> mapper(string line) {
    vector<int> res;
    for (auto c: line) {
        if ('a' <= c && c <= 'z') res.push_back(1 << (c - 'a'));
        else if ('A' <= c && c <= 'Z') res.push_back(-(1 << (c - 'A')));
        else if (c == '@') res.push_back(1 << 30);
        else if (c == '#') res.push_back(-(1 << 27));
        else res.push_back(0);
    }
    return res;
}

using Pos = pair<vector<int>, int>;

int get_reachable_keys(vector<int> grid, Coord start) {
    vector<Coord> q;
    q.push_back(start);
    auto children = [&](Coord node)  {
        return vector<Coord>{node.up(), node.left(), node.right(), node.down()};
    };
    int key = 0;
    vector<int> dist(total,-1);
    dist[start] = 0;
    while (q.size()) {
        auto node = q.back(); q.pop_back();
        int val = grid[node]; if (val > 0) key |= val;
        for (auto child: children(node)) {
            if (child < 0 || child >= n) continue;
            if (grid[child] == -(1 << 27)) continue;
            if (dist[child] != -1) continue;
            dist[child] = dist[node] + 1;
            q.push_back(child);
        }
    }
    return key;
}

int get_all_keys(const vector<int> &grid) {
    int result = 0;
    for (auto x : grid) {
        if (x > 0) result |= x;
    }
    return result;
}

auto directions = [&](Coord start) {
    return vector<Coord>{start.left(), start.up(), start.down(), start.right()};
};

int get_dist(vector<int> grid, vector<int> start) {
    int target = get_all_keys(grid);

    int keys[start.size()] = {};
    for (size_t _i = 0; _i < start.size(); ++_i) {
        keys[_i] = get_reachable_keys(grid, Coord{start[_i]});
    }

    auto children2 = [&](Coord start, int key) {
        vector<vector<int>> results;
        vector<Coord> q;
        q.push_back(start);
        memset(dist, -1, sizeof(dist));
        dist[start] = 0;
        size_t idx = 0;
        while (idx < q.size()) {
            auto node = q[idx++];
            int new_key = grid[node];
            if (new_key > 0 && (new_key & key) == 0) {
                results.push_back({node, key | new_key, dist[node]});
                continue;
            }

            for (auto child: directions(node)) {
                if (child < 0 || child >= total) continue;
                if (grid[child] < 0 && (key & -grid[child]) == 0) continue;
                if (dist[child] != -1) continue;
                dist[child] = dist[node] + 1;
                q.push_back(child);
            }
        }
        return results;
    };

    auto children = [&](Pos nodes) {
        vector<pair<Pos, int>> results;
        for (size_t _i = 0; _i < nodes.first.size(); ++_i) {
            /* if ((keys[_i] & nodes[8]) == keys[_i]) continue; */
            int off = _i;
            for (auto res: children2(Coord{nodes.first[off]}, nodes.second)) {
                Pos newnodes = nodes;
                newnodes.first[off] = res[0];
                newnodes.second = res[1];
                results.push_back({newnodes, res[2]});
            }
        }
        return results;
    };
    using State = pair<vector<int>, int>;
    State init{start, 0};

    set<pair<int, Pos>> q;
    map<Pos, int> dist;
    dist[init] = 0;
    q.insert({dist[init], init});
    size_t i = 0;
    while (q.size()) {
        i++;
        auto p = *q.begin(); q.erase(q.begin());
        Pos node = p.second;
        /* if (i % 10000 == 0) cout << i << " " << __builtin_popcount(target) << " " << __builtin_popcount(target & node.second) << endl; */
        if ((node.second & target) == target) {
            return dist[node];
        }

        for (auto ans: children(node)) {
            auto child = ans.first; auto newdist = ans.second;
            if (dist.find(child) != dist.end() && dist[child] <= dist[node] + newdist) continue;
            dist[child] = dist[node] + newdist;
            q.insert({dist[child], child});
        }
    }
    cout << "Reached end" << endl;
    return -1;
}

int main() {
    string line;
    vector<int> grid;
    while (cin >> line) {
        auto newline = mapper(line);
        grid.insert(grid.end(), newline.begin(), newline.end());
    }

    Coord start=-1;
    for (int idx = 0; idx < total; ++idx) {
        if (grid[idx] == 1 << 30) {
            start=idx;break;
        }
    }
    grid[start] = 0;

    cout << "Part 1: " << get_dist(grid, {start}) << endl;


    grid[start] = -(1 << 27);
    grid[start.right()] = -(1 << 27);
    grid[start.left()] = -(1 << 27);
    grid[start.up()] = -(1 << 27);
    grid[start.down()] = -(1 << 27);

    grid[start.up().left()] = 0;
    grid[start.up().right()] = 0;
    grid[start.down().left()] = 0;
    grid[start.down().right()] = 0;

    vector<int> start_pos{start.up().left(), start.up().right(), start.down().left(), start.down().right()};

    cout << "Part 2: " << get_dist(grid, start_pos) << endl;
}
