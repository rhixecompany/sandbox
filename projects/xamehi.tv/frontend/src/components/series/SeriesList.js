<<<<<<< HEAD
import React from "react";
import {
  List,
  Datagrid,
  TextField,
  ImageField,
  DateField,
  EditButton,
  DeleteButton,
} from "react-admin";

function SeriesList(props) {
  return (
    <List {...props}>
      <Datagrid>
        <TextField source="_id" />
        <ImageField source="image" />
        <TextField source="name" />
        <DateField source="updateAt" />
        <EditButton basePath="/movies" />
        <DeleteButton basePath="/movies" />
      </Datagrid>
    </List>
  );
}

export default SeriesList;
=======
import React from "react";
import {
  List,
  Datagrid,
  TextField,
  ImageField,
  DateField,
  EditButton,
  DeleteButton,
} from "react-admin";

function SeriesList(props) {
  return (
    <List {...props}>
      <Datagrid>
        <TextField source="_id" />
        <ImageField source="image" />
        <TextField source="name" />
        <DateField source="updateAt" />
        <EditButton basePath="/movies" />
        <DeleteButton basePath="/movies" />
      </Datagrid>
    </List>
  );
}

export default SeriesList;
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
