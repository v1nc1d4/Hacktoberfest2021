import java.util.Scanner;
class Q3{
	public static void main(String[] args)
	{
		Scanner r=new Scanner(System.in);
		System.out.println("Enter a sentence");
		String str=r.nextLine();
		str+=" ";
		String longw="";
		String temp="";
		int index=0;
		for(int i=0;i<str.length();i++){	
			if(str.charAt(i)==' '){
				if(temp.length()>longw.length()){
					longw=temp;
					temp="";
					index=i-longw.length();
				}
				else temp="";
			}
			else temp=temp+str.charAt(i);
		}
		
		System.out.println("The largest word is: " + longw);
		System.out.println("The index number is: " +index);
		r.close();
	}
} 
