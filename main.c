#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#define MAXCHAR 1000
#define max 100


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
    printf("\nAccount created successfully!");
}

void checkProfile()
{
    printf("\n\nPlease provide your login credentials");
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
        printf("Please verify your account details and try again...\n");
    }
}

void deleteProfile()
{
    printf("\nEnter details to delete your account");
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
            deleteAccount(details);
            printf("Your account has been successfully deleted!");
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
        printf("Please verify your account details and try again...\n");
    }
}

void deleteAccount(char *account)
{
    char temp_a[max][max];
    int temp_top = -1;
    char temp_x[max];
    int i;
    for(i=0;i<top+1;i++)
    {
        if(strcmp(a[i],account) != 0)
        {
            temp_top++;
            strcpy(temp_a[temp_top],a[i]);
        }
    }

    top = -1;
    for(i=0;i<temp_top+1;i++)
    {
        top++;
        strcpy(a[top],temp_a[i]);
    }
}

int main()
{
    FILE *fp;
    char accountExists[3];
    char str[MAXCHAR];
    char* filename = "Logo.txt";

    fp = fopen(filename, "r");
    while (fgets(str, MAXCHAR, fp) != NULL)
        printf("%s", str);
    fclose(fp);

    printf("______________________________________________________________");
    printf("\n\nHey! Welcome to Health tracker");
    printf("\nDo you already have an account?(yes/no) : ");
    scanf("%s", accountExists);
    if(strcmp(accountExists,"Yes") == 0 || strcmp(accountExists,"yes") == 0 || strcmp(accountExists,"y") == 0)
    {
        int choice;
        push("gokul : password");
        push("hello : world");
        push("health : tracker");
        printf("\nWhat would you like to do?(1/2)\n1) Login\n2) Delete account\nYour choice > ");
        scanf("%d", &choice);
        if(choice == 1)
        {
            checkProfile();
        }
        else if(choice == 2)
        {
            deleteProfile();
            checkProfile();
        }
        else
        {
            printf("\nWrong choice. Enter either \"1\" or \"2\".\n");
        }
    }
    else if(strcmp(accountExists,"No") == 0 || strcmp(accountExists,"no") == 0 || strcmp(accountExists,"n") == 0)
    {
        createProfile();
        checkProfile();
    }
    else
    {
        printf("\nWrong choice. Enter either \"yes\" or \"no\".\n");
    }
    return 0;
}
