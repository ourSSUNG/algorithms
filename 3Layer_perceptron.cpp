#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define c 0.5 //learning rate
#define DIMENSION 2 //input 갯수
#define LAYER_NUM 2 //layer 수
#define NODE_NUM 2 //layer당 node 수
#define TRAINING_SET 9//training data의 갯수

float weights[DIMENSION + 1]; //weights들을 저장한 배열
int iterationNum = 0; //Error그래프를 만들기위해서 필요한 변수

float train_set_x[][2] = {
{0.,0.},
{0.,1.},
{1.,0.},
{1.,1.},
{0.5,1.},
{1.,0.5},
{0.,0.5},
{0.5,0.},
{0.5,0.5} };
float train_set_y[] = { 0,0,0,0,0,0,0,0,1 };

//퍼셉트론 구조체
struct Perceptron {
	float weights[DIMENSION+1];
	float current_NET;
	float current_Sigmoid;
	float current_delta;
};

struct Perceptron PerArray[LAYER_NUM][NODE_NUM];
struct Perceptron Out;

int weightsMarker() {
	FILE* pfile;
	fopen_s(&pfile, "weights.txt", "wt");
	for (int i = 0; i < LAYER_NUM; i++) {
		for (int j = 0; j < NODE_NUM; j++) {
			fprintf(pfile, "[");
			for (int k = 0; k < DIMENSION + 1; k++) {
				fprintf(pfile,"%f ", PerArray[i][j].weights[k]);
			}
			fprintf(pfile, "]");
		}
		fprintf(pfile, "\n");
	}
	for (int i = 0; i < DIMENSION + 1; i++) {
		fprintf(pfile, "%f ", Out.weights[i]);
	}
	fclose(pfile);
	return 0;
}

int PerMaker(){
	for (int i = 0; i < LAYER_NUM; i++) {
		for (int j = 0; j < NODE_NUM; j++) {
			for (int k = 0; k < DIMENSION + 1; k++) {
				PerArray[i][j].weights[k] = (rand()-16000)/16000.0;
				//일단 perceptron의 모든 weight들을 random값으로 초기화
			}
		}
	}
	for (int i = 0; i < DIMENSION + 1; i++) {
		Out.weights[i] = 1;
	}
	return 0;
}


int test() {
	float error = 0.0;
	for (int i = 0; i < TRAINING_SET; i++) {
		float *input = train_set_x[i];
		float output = train_set_y[i];
		for (int j = 0; j < LAYER_NUM; j++) {
			for (int k = 0; k < NODE_NUM; k++) {
				float net = 0;
				if (j == 0) {
					for (int l = 0; l < DIMENSION; l++) {
						net += input[l] * PerArray[j][k].weights[l];
					}
					net += PerArray[j][k].weights[DIMENSION];
					
				}
				else {
					for (int l = 0; l < DIMENSION; l++) {
						net += PerArray[j-1][l].current_Sigmoid * PerArray[j][k].weights[l];
					}
					net += PerArray[j][k].weights[DIMENSION];
				}
				PerArray[j][k].current_NET = net;
				float sig = 1 / (1 + exp(-net));				
				PerArray[j][k].current_Sigmoid = sig;
				
			}
		}
		float result = 0;
		for (int i = 0; i < NODE_NUM; i++) {
			result += PerArray[LAYER_NUM - 1][i].current_Sigmoid*Out.weights[i];
		}
		result += Out.weights[DIMENSION];
		Out.current_NET = result;
		float sig = 1 / (1 + exp(-result));
		Out.current_Sigmoid = sig;		
		error += (output - sig)*(output - sig) / 2.0;
	}
	printf("%f\n", error);
	return 0;
}

//out layer의 퍼셉트론학습 전용 함수
int OutLayerLearning(float target) {
	float delta = (target - Out.current_Sigmoid) * Out.current_Sigmoid*(1 - Out.current_Sigmoid);
	for (int i = 0; i < DIMENSION; i++) {
		Out.weights[i] += c * delta * PerArray[LAYER_NUM - 1][i].current_Sigmoid;
	}
	Out.weights[DIMENSION] += c * delta;
	Out.current_delta = delta;
	return 0;
}

//out layer 바로 직전 계층의 학습용 함수
int preOutLayerLearning() {
	for (int i = 0; i < NODE_NUM; i++) {
		float delta = Out.current_delta * Out.weights[i] * PerArray[LAYER_NUM - 1][i].current_Sigmoid * (1 - PerArray[LAYER_NUM - 1][i].current_Sigmoid);
		for (int j = 0; j < DIMENSION; j++) {
			PerArray[LAYER_NUM - 1][i].weights[j] += c * delta*PerArray[LAYER_NUM - 2][j].current_Sigmoid;
		}
		PerArray[LAYER_NUM - 1][i].weights[DIMENSION] += c * delta;
		PerArray[LAYER_NUM - 1][i].current_delta = delta;
	}
	return 0;
}

//hidden layer의 학습용 함수
int hiddenLearning(int layer) {
	for (int i = 0; i < NODE_NUM; i++) {
		float delta = 0.0;
		for (int j = 0; j < NODE_NUM; j++) {
			delta += PerArray[layer + 1][j].current_delta * PerArray[layer + 1][j].weights[i];
		}
		delta *= PerArray[layer][i].current_Sigmoid*(1 - PerArray[layer][i].current_Sigmoid);
		for (int j = 0; j < DIMENSION; j++) {
			PerArray[layer][i].weights[j] += c * delta * PerArray[layer - 1][j].current_Sigmoid;
		}
		PerArray[layer][i].weights[DIMENSION] += c * delta;
		PerArray[layer][i].current_delta = delta;
	}
	return 0;
}

//input layer의 학습용 함수
int InputLayerLearning(float *inputs) {
	for (int i = 0; i < NODE_NUM; i++) {
		float delta = 0.0;
		for (int j = 0; j < NODE_NUM; j++) {
			delta += PerArray[1][j].current_delta * PerArray[1][j].weights[i];
		}
		delta *= PerArray[0][i].current_Sigmoid*(1 - PerArray[0][i].current_Sigmoid);
		for (int j = 0; j < DIMENSION; j++) {
			PerArray[0][i].weights[j] += c * delta * inputs[j];
		}
		PerArray[0][i].weights[DIMENSION] += c * delta;
		PerArray[0][i].current_delta = delta;
	}
	return 0;
}

//sigmoid값 설정을 위한 함수입니다
int sigSetting(float * input, float output) {
	for (int i = 0; i < NODE_NUM; i++) {
		float net = 0;
		for (int j = 0; j < DIMENSION; j++) {
			net += input[j] * PerArray[0][i].weights[j];
		}
		net += PerArray[0][i].weights[DIMENSION];
		float sig = 1 / (1 + exp(-net));
		PerArray[0][i].current_Sigmoid = sig;
	}
	for (int i = 1; i < LAYER_NUM; i++) {
		for (int j = 0; j < NODE_NUM; j++) {
			float net = 0;
			for (int k = 0; k < DIMENSION; k++) {
				net += PerArray[i][j].weights[k] * PerArray[i - 1][k].current_Sigmoid;
			}
			net += PerArray[i][j].weights[DIMENSION];
			float sig = 1 / (1 + exp(-net));
			PerArray[i][j].current_Sigmoid = sig;
		}
	}
	float net = 0;
	for (int i = 0; i < NODE_NUM; i++) {
		net += Out.weights[i] * PerArray[LAYER_NUM - 1][i].current_Sigmoid;
	}
	net += Out.weights[DIMENSION];
	float sig = 1 / (1 + exp(-net));
	Out.current_Sigmoid = sig;
	return 0;
}

//도우넛 데이터 학습을 위한 함수입니다
int dataLearning() {
	//인풋 데이터 수만큼 전부 학습
	for (int i = 0; i < TRAINING_SET; i++) {
		sigSetting(train_set_x[i], train_set_y[i]);
		for (int j = LAYER_NUM; j >= 0; j--) {
			if (j == LAYER_NUM) {
				OutLayerLearning(train_set_y[i]);
			}
			else if (j == LAYER_NUM - 1) {
				preOutLayerLearning();
			}
			else if (j != 0) {
				hiddenLearning(j);
			}
			else {
				InputLayerLearning(train_set_x[i]);
			}
		}
	}
	return 0;
}


int main() {
	PerMaker();
	test();
	for (int i = 0; i < 100000; i++) {
		dataLearning();
		test();
	}
	weightsMarker();
	for (int i = 0; i < TRAINING_SET; i++) {
		sigSetting(train_set_x[i], train_set_y[i]);
		printf("%f %f\n", train_set_y[i], Out.current_Sigmoid);
	}


	return 0;
}
