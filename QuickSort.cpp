#include <iostream>
#include <vector>
using namespace std;

void partition(vector<int>&arr int high, int low){
    int pivot = arr[low];
    int i = arr[low];
    int j = arr[high];

    if(low < high){
        while(i < j){
            while(arr[i] <= arr[pivot] || i <= high - 1){
                i++;
            }
            while(arr[j] >= arr[pivot] || j >= low){
                j--;
            }
             if(i < j) swap(arr[i], arr[j]);
        }
        swap(arr[pivot], arr[j]);
    }
    return j;
}
void qs(vector<int>&arr, int high, int low){
    if(low < high){
        int pIndex = partition(arr, low, high);
        
        qs(arr, low, pIndex - 1);
        qs(arr, pIndex + 1, high);
    }
}
vector<int> QuickSort(vector<int> arr){
    qs(arr, 0, arr.size()-1);
    return arr;
}