/*Write a java program to get ‘n’ elements in an array. Perform the linear and binary search.*/
import java.util.*;
class Q1{
	static int binS(int ele,int l,int r, int arr[]){
		if(r>=l){
			int mid=l+(r-l)/2;
			if(arr[mid]==ele) return mid;
			else if(arr[mid]>ele) return binS(ele,l,mid-1,arr);
			else return binS(ele,mid+1,r,arr);
		}
		else return -1;
		
	}
	static int linS(int ele,int arr[],int n){
		for(int x=0;x<n;x++){
			if(arr[x]==ele) return x;
		}
		return -1;
	}
	public static void main(String []args){
		Scanner sobj = new Scanner(System.in);
		System.out.println("Enter n value: ");
		int n = sobj.nextInt();
		int []arr = new int[n];
		for(int i=0;i<n;i++){
			System.out.println("Enter element" + (i+1)+": ");
			arr[i] = sobj.nextInt();
		}
		System.out.println("Enter element to be found: ");
		int ele = sobj.nextInt();
		System.out.println("Input Array:\n"+Arrays.toString(arr));
		int pos2 = linS(ele,arr,n);
		System.out.println("using ls ele found at "+pos2);
		Arrays.sort(arr);
		System.out.println("After Sorting:\n"+Arrays.toString(arr));
		int pos1 = binS(ele,0,n-1,arr);
		System.out.println("using bs ele found at "+pos1);
		sobj.close();
		
	}
}
