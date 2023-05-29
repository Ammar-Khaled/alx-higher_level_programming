#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints bytes info
 * @p: pointer to python object
 */
void print_python_bytes(PyObject *p)
{
    long int size, max_printed, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    printf("  size: %ld\n", size);

    str = ((PyBytesObject *)p)->ob_sval;
    printf("  trying string: %s\n", str);

    if (size >= 10)
    {
        max_printed = 10;
    }
    else
    {
        max_printed = size + 1;
    }

    printf("  first %ld bytes:", max_printed);

    for (i = 0; i < max_printed; i++)
    {
        if (str[i] >= 0)
        {
            printf(" %02x", str[i]);
        }
        else
        {
            printf(" %02x", str[i] + 256);
        }
        
    }
    printf("\n");
}

/**
 * print_python_list - print list info
 * @p: pointer to python object
 */
void print_python_list(PyObject *p)
{
    long int size, i;
    PyListObject *list;
    PyObject *item;

    printf("[*] Python list info\n");

    size = ((PyVarObject *)p)->ob_size;
    printf("[*] Size of the Python List = %ld\n", size);

    list = (PyListObject *)p;
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        item = list->ob_item[i];
        printf("Element %ld: %s\n", i, (item->ob_type)->tp_name);
        if (PyBytes_Check(item))
        {
            print_python_bytes(item);
        }
    }
}
