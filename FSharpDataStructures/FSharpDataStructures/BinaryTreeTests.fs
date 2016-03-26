module BinaryTreeTests

open System
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

[<EntryPoint>]
let printTraversals argc =
    BinaryTree.printInOrder binTree1
    printfn "\n" 
    BinaryTree.printPostOrder binTree1
    printfn "\n"
    BinaryTree.printPreOrder binTree1
    printfn "\n"
    Console.ReadKey() |> ignore
    0 