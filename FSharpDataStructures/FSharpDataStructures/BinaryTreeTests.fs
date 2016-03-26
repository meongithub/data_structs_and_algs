module BinaryTreeTests

open BinaryTree

(*
     2
    / \
   1   4
  / \
 3  5

*)
let binTree1 = 
    BinaryTree.Node(2, 
                    BinaryTree.Node(1, 
                                    BinaryTree.Node(3, Empty, Empty), 
                                    BinaryTree.Node(5, Empty, Empty)), 
                    BinaryTree.Node(4, Empty, Empty))
