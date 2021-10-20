class Q2{
	static void printMat(int[][] mat, int r,int c){
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				System.out.print(mat[i][j]+" ");
			}
			System.out.println(" ");
		}
	}
	static void add(int[][] a, int[][] b, int r, int c){
		int[][] res = new int[r][c]; 
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				res[i][j]=a[i][j]+b[i][j];
			}
		}
		printMat(res,r,c);
	}
	
	static void sub(int[][] a, int[][] b, int r, int c){
		int[][] res = new int[r][c]; 
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				res[i][j]=a[i][j]-b[i][j];
			}
		}
		printMat(res,r,c);
	}	
	
	static void multiply(int[][] m1, int[][] m2, int r1, int c1, int r2, int c2){
		if(c1!=r2) System.out.println("Cannot multiply");
		else{
			int[][] res = new int[r1][c2];
			int sum;
			for(int i=0;i<r1;i++){
				for(int j=0;j<c2;j++){
					sum=0;
					for(int k=0;k<c1;k++){
						sum+=m1[i][k] * m2[k][j];
					}
					res[i][j] = sum;
				}
			}
			printMat(res,r1,c2);
		}
	}
	public static void main(String[] args){
		int[][] a = {{1,2,3},{4,5,6}};
		int[][] b = {{10,11},{20,21},{30,31}};
		System.out.println("Matrix A:");
		printMat(a, 2, 3);
		System.out.println("Matrix B:");
		printMat(b, 3, 2);
		System.out.println("A X B:");
		multiply(a,b,2,3,3,2);
		int[][] c = {{1,1,1},{1,1,1}};
		System.out.println("Matrix A:");
		printMat(a, 2, 3);
		System.out.println("Matrix B:");
		printMat(c, 2, 3);;
		System.out.println("A + B:");
		add(a, c, 2, 3);
		System.out.println("A - B:");
		sub(a, c, 2, 3);

	}
}
