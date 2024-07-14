```cpp
#include <iostream>
#include <SDL.h>
#include <time.h>

using namespace std;

SDL_Window* win = NULL;
SDL_Renderer* r = NULL;
SDL_Surface* img = NULL;
SDL_Rect src_rect;
SDL_Rect dst_rect;

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
	r = SDL_CreateRenderer(win, -1, SDL_RENDERER_SOFTWARE);
}

void render_rect() {
	SDL_SetRenderDrawColor(r, 0, 0, 0, 0);
	SDL_Rect rect = { 100, 100, 400, 400 };
	SDL_RenderDrawRect(r, &rect);

	SDL_Rect rect1 = { 200, 200, 200, 200 };
	SDL_RenderFillRect(r, &rect1);
}

void load_img(int width, int height) {
	img = SDL_LoadBMP("./1.bmp");
	cout << img->w << " " << img->h << endl;
	src_rect = SDL_Rect{ 0,0,img->w,img->h };
	dst_rect = SDL_Rect{ 0,0,width, height };
}

void render_image() {
	SDL_Texture* mm = SDL_CreateTextureFromSurface(r, img);

	//SDL_RenderCopy(r, mm, &src_rect,  &dst_rect);
	SDL_RenderCopy(r, mm, &src_rect, &dst_rect);
	SDL_DestroyTexture(mm);
}

void event_loop() {
	bool isrunning = true;
	while (isrunning) {
		//消息模块
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
				if (msg.button.button == SDL_BUTTON_LEFT) {
					if (dst_rect.w > 2 && dst_rect.h > 2) {
						dst_rect.w /= 2;
						dst_rect.h /= 2;
					}
					//cout << "鼠标左键\n";
				}
				if (msg.button.button == SDL_BUTTON_RIGHT) {
					dst_rect.w *= 2;
					dst_rect.h *= 2;
					//cout << "鼠标右键\n";
				}
				break;
			case SDL_MOUSEMOTION:
				//cout << "鼠标移动\n";
				break;
			}
		}
		//绘图模块
		SDL_SetRenderDrawColor(r, 255, 0, 0, 0);
		SDL_RenderClear(r);
		//其他绘图
		//render_rect();

		render_image();
		SDL_RenderPresent(r);
	}
}

//定时器
bool on_timer(int duration) {
	static int start = clock();
	int end = clock();
	if (end - start >= duration) {
		start = end;
		return true;
	}
	return false;
}

signed main(int argc, char* argv[]) {
	init_sdl();
	creat_window(800, 500);
	load_img(800, 500);
	event_loop();
	return 0;
}
```
