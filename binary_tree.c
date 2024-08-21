#include "c_utils.h"


typedef struct node_t {
    int val;
    struct node_t *left;
    struct node_t *right;
} node_t;

void insert(node_t *root, node_t *node) {
    if (node->val == root->val) {
        free(node);
        return;
    }

    if (node->val < root->val) {
        if (root->left) {
            insert(root->left, node);
        } else {
            root->left = node;
        }
    } else {
        if (root->right) {
            insert(root->right, node);
        } else {
            root->right = node;
        }
    }
}

node_t *build_tree(int size) {
    node_t *root, *node;
    int mod = 100;

    root = (node_t *)malloc(sizeof(node_t));
    root->left = root->right = NULL;
    root->val = rand() % mod;

    for (int i = 0; i < size - 1; i++) {
        node = (node_t *)malloc(sizeof(node_t));
        node->left = node->right = NULL;
        node->val = rand() % mod;
        insert(root, node);
    }

    return root;
}

int tree_size(node_t *root) {
    int size = 0;

    if (root->left) {
        size += tree_size(root->left);
    }

    if (root->right) {
        size += tree_size(root->right);
    }

    size += 1;

    return size;
}

void print_preorder(node_t *root) {
    if (root->left) {
        print_preorder(root->left);
    }
    printf("%d\n", root->val);

    if (root->right) {
        print_preorder(root->right);
    }
}

void print_desc(node_t *root) {
    if (root->right) {
        print_desc(root->right);
    }

    printf("%d\n", root->val);

    if (root->left) {
        print_desc(root->left);
    }
}

bool search(node_t *root, int val) {
    if (root->val == val) {
        return true;
    } else if (val < root->val) {
        if (root->left) {
            return search(root->left, val);
        }
    } else {
        if (root->right) {
            return search(root->right, val);
        }
    }

    return false;
}

int shortest_path(node_t *root) {
    int left, right;
    left = right = 0;

    if (root->left) {
        left = 1 + shortest_path(root->left);
    }

    if (root->right) {
        right = 1 + shortest_path(root->right);
    }

    if (left && right) {
        return MIN(left, right);
    }

    return MAX(left, right);
}

int longest_path(node_t *root) {
    int left, right;
    left = right = 0;

    if (root->left) {
        left = 1 + longest_path(root->left);
    }

    if (root->right) {
        right = 1 + longest_path(root->right);
    }

    return MAX(left, right);
}

void print_level(node_t *root, int width, int level, int target_level) {
    if (!root || level > target_level) {
        return;
    }

    if (level < target_level) {
        if (root->left) {
            print_level(root->left, width, level + 1, target_level);
        } else {
            printf("%*s", width * (int)pow(2, target_level - level - 1), "");
        }

        if (root->right) {
            print_level(root->right, width, level + 1, target_level);
        } else {
            printf("%*s", width * (int)pow(2, target_level - level - 1), "");
        }
    } else { // correct level
        // center jusitfy text
        printf("%*d%*s", width / 2, root->val, width - width / 2, "");
    }
}

void print_level_connectors(node_t *root, int width, int level, int target_level) {
    if (!root || level > target_level) {
        return;
    }

    if (level < target_level) {
        if (root->left) {
            print_level_connectors(root->left, width, level + 1, target_level);
        } else {
            printf("%*s", width * (int)pow(2, target_level - level - 1), "");
        }

        if (root->right) {
            print_level_connectors(root->right, width, level + 1, target_level);
        } else {
            printf("%*s", width * (int)pow(2, target_level - level - 1), "");
        }
    } else {
        if (root->left) {
            printf("%*s/%*s", width / 4, "", width / 4, "");
        } else {
            printf("%*s", width / 2, "");
        }

        if (root->right) {
            printf("%*s\\%*s", width / 8, "", width / 4, "");
        } else {
            printf("%*s", width - width / 2, "");
        }
    }
}

void print_tree(node_t *root) {
    int height = longest_path(root);
    int width = 100;

    for (int i = 0; i <= height; i++) {
        print_level(root, width, 0, i);
        printf("\n");
        print_level_connectors(root, width, 0, i);
        printf("\n");
        width /= 2;
    }

    printf("\n");
}

int smallest(node_t *root) {
    if (root->left) {
        return smallest(root->left);
    }

    return root->val;
}

int * _nthSmallest(node_t *root, int n) {
    int *res;

    if (root->left) {
        res = _nthSmallest(root->left, n);

        if (res[1] < 1) {
            return res;
        }

        n = res[1];
    }

    // this node
    n -= 1;

    if (n >= 1 && root->right) {
        res = _nthSmallest(root->right, n);
    } else {
        res = malloc(sizeof(int) * 2);
        res[0] = root->val;
        res[1] = n;
    }

    return res;
}

int nthSmallest(node_t *root, int n) {
    int *res = _nthSmallest(root, n);

    if (res[1] < 1) {
        return res[0];
    }

    return -1;
}

int main(int argc, char **argv) {
    srand(1);
    node_t *root = build_tree(17);
    print_tree(root);

    printf("preorder\n");
    print_preorder(root);

    printf("smallest: %d\n", smallest(root));
    printf("nthSmallest(2): %d\n", nthSmallest(root, 2));
    printf("nthSmallest(3): %d\n", nthSmallest(root, 3));
    printf("nthSmallest(4): %d\n", nthSmallest(root, 4));
    printf("nthSmallest(5): %d\n", nthSmallest(root, 5));

    // printf("\ndesc\n");
    // print_desc(root);
    // printf("\n\n");


    int n = 9;
    bool res = search(root, n);
    printf("search(%d) = %s\n", n, res ? "true" : "false");

    printf("shortest_path = %d\n", shortest_path(root));
    printf("longest_path = %d\n", longest_path(root));

    return 0;
}


// watch 'gcc binary_tree.c -o binary_tree && ./binary_tree'
