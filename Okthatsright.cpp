// Okthatsright.cpp: определяет точку входа для консольного приложения.
//

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int dx[] = { -2, -2, 2, 2, 1, -1, 1, -1 };
const int dy[] = { -1, 1, -1, 1, 2, -2, -2, 2 };
const size_t N = 100;

int main()
{
	setlocale(LC_ALL, "Russian");
	bool doska[N][N]; 


	for (int i = 0; i < N; i++)
	for (int j = 0; j < N; j++)
		doska[i][j] = 0;             
	int x1, y1;                          
	cin >> x1 >> y1;
	doska[x1 - 1][y1 - 1] = 1;      
	int x2, y2;                
	cin >> x2 >> y2;
	vector <pair <int, int> > data; 
	queue <pair <pair <int, int>, vector <pair <int, int> > > > queuew;
	queuew.push(make_pair(make_pair(x1 - 1, y1 - 1), data));
	

	/*
	for (int x = 0; x < N; x++){
		for (int y = 0; y < N; y++){
			if (x == x1 & y == y1){
				doska[x][y] = 0;
			}
			for (int i = 0; i < 8; i++){
				if (x + dx[i] < N & y + dy[i] < N) {
					if (doska[x + dx[i]][y + dy[i]] != 0) {
						doska[x][y] = doska[x + dx[i]][y + dy[i]] + 1;
					}
				}

			}
		}
	}

	cout << "Наименьшее количество ходов: " << doska[x2-1][y2-1] << endl;

	*/

	while (!queuew.empty()) 
	{
		pair <int, int> now = queuew.front().first; 
		data = queuew.front().second;                
		if (now.first == x2 - 1 && now.second == y2 - 1) break;
		queuew.pop(); 
		for (int i = 0; i < 8; i++)
		{
			if (now.first + dx[i] < N && now.first + dx[i] >= 0 &&
				now.second + dy[i] < N && now.second + dy[i] >= 0 &&
				doska[now.first + dx[i]][now.second + dy[i]] == 0)
			{
				vector <pair <int, int> > data2 = data;
				data2.push_back(make_pair(now.first + dx[i], now.second + dy[i]));
				queuew.push(make_pair(make_pair(now.first + dx[i], now.second + dy[i]), data2));
				doska[now.first + dx[i]][now.second + dy[i]] = 1;	
			}
		}
	} 



	cout << "Наименьшее количество ходов: " << data.size() << endl;
	cout << "Правильные ходы:" << endl;
	for (int i = 0; i < data.size(); i++)
		cout << data[i].first + 1 << " " << data[i].second + 1 << endl;
	system("pause");
	return 0;
}

