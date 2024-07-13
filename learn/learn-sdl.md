```cpp
#include <iostream>
#include <SDL.h>

using namespace std;

SDL_Window* win = NULL;
SDL_Renderer* p = NULL;

void init_sdl() {
	if (SDL_Init(SDL_INIT_EVERYTHING) != 0) {
		SDL_Log("%s", SDL_GetError());
	}
}

void studyDateType() {
	SDL_Point point;
	SDL_Rect rect;
	SDL_Color color;

	SDL_Window* window = NULL;  //窗口指针
	SDL_Renderer* render = NULL;//渲染器

	SDL_Surface* surface = NULL;//图像
	SDL_Texture* texture = NULL;//纹理

	SDL_Event msg;		//事件
	msg.type;			//区分类型
	msg.motion.x;		//x和y的坐标
	msg.motion.y;
	msg.key.keysym.sym;	//按键的值
	msg.button.button;	//鼠标按键分类
}

void creat_window(int w, int h) {
	win = SDL_CreateWindow("cool", 100, 100, w, h, SDL_WINDOW_SHOWN);

}

void event_loop() {
	bool isrunning = true;
	while (isrunning) {
		SDL_Event msg;
		if (SDL_WaitEvent(&msg) != 0) {
			switch (msg.type) {
			case SDL_QUIT:
				isrunning = false;
				break;
			case SDL_KEYDOWN:
				printf("%c\n", msg.key.keysym.sym);
				break;
			case SDL_MOUSEBUTTONDOWN:
				if (msg.button.button == SDL_BUTTON_LEFT)
					cout << "鼠标左键\n";
				if (msg.button.button == SDL_BUTTON_RIGHT)
					cout << "鼠标右键\n";
				break;
			case SDL_MOUSEMOTION:
				cout << "鼠标移动\n";
				break;
			}
		}
	}
}

signed main(int argc, char* argv[]) {
	init_sdl();
	creat_window(800, 500);
	event_loop();
	return 0;
}
```
