#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#define MAXCHAR 1000
#define max 10


char a[max][max];
int top = -1;
char x[max];
char username[20];
char password[20];

void push();
int pop();
void display();

void push(char *x)
{
    top++;
    strcpy(a[top],x);
}

int pop()
{
    strcpy(x,a[top]);
    top--;
}

void display()
{
    int i;
    for(i=0;i<top+1;i++)
    {
        printf("%s \n",a[i]);
    }
}

void createProfile()
{
    printf("\nCreating your profile");
    printf("\nEnter your new Username: ");
    scanf("%s", username);
    printf("Create your password: ");
    scanf("%s", password);
    char details[100];
    strcpy(details, "");
    strcat(details, username);
    strcat(details, " : ");
    strcat(details, password);
    push(details);
    printf("\nAccount created successfully!\n");
}

void checkProfile()
{
    printf("\nPlease provide your login credentials");
    printf("\nUsername: ");
    scanf("%s", username);
    printf("Password: ");
    scanf("%s", password);
    char details[100];
    strcpy(details, "");
    strcat(details, username);
    strcat(details, " : ");
    strcat(details, password);
    int i;
    int check = 0;
    for(i=0;i<top+1;i++)
    {
        if(strcmp(a[i],details) == 0)
        {
            printf("Logged in Successfully!");
            check = 1;
            break;
        }
        else
        {
            check = 0;
        }
    }
    if(check == 0)
    {
        printf("Please check your username and password again...");
    }
}

int main()
{
    FILE *fp;
    char accountExists[3];
    char str[MAXCHAR];
    char* filename = "Logo.txt";

    fp = fopen(filename, "r");
    if (fp == NULL){
        printf("Could not open file %s",filename);
        return 1;
    }
    while (fgets(str, MAXCHAR, fp) != NULL)
        printf("%s", str);
    fclose(fp);
    printf("______________________________________________________________");
    printf("\n\nHey! Welcome to Health tracker");
    printf("\nDo you already have an account?(yes/no) : ");
    scanf("%s", accountExists);
    if(strcmp(accountExists,"Yes") == 0 || strcmp(accountExists,"yes") == 0 || strcmp(accountExists,"y") == 0)
    {
        push("gokul : password");
        checkProfile();
    }
    else if(strcmp(accountExists,"No") == 0 || strcmp(accountExists,"no") == 0 || strcmp(accountExists,"n") == 0)
    {
        createProfile();
        checkProfile();
    }
    else
    {
        printf("\nWrong choice. Enter either \"yes\" or \"no\".");
    }
    return 0;
}s
