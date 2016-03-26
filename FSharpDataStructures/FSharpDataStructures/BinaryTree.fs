module BinaryTree

type BinaryTree =
     | Node of int * BinaryTree * BinaryTree
     | Empty

let rec printInOrder tree =
    match tree with 
    | Node (data, left, right)
        -> printInOrder left
           printfn "Node %d" data
           printInOrder right
    | Empty
        -> ()

let rec printPreOrder tree =
    match tree with
    | Node (data, left, right)
        -> printfn "Node %d" data
           printPreOrder left
           printPreOrder right
    | Empty
        -> ()

let rec printPostOrder tree =
    match tree with
    | Node (data, left, right)
        -> printPostOrder left
           printPostOrder right
           printfn "Node %d" data
    | Empty
        -> ()