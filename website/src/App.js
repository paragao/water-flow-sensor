import React, { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

//Material-UI
import 'fontsource-roboto';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import MenuItem from '@material-ui/core/MenuItem';
import Snackbar from '@material-ui/core/Snackbar';
import MuiAlert from '@material-ui/lab/Alert';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TablePagination from '@material-ui/core/TablePagination';
import TableRow from '@material-ui/core/TableRow';
import { Menu, Typography } from '@material-ui/core';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import TextField from '@material-ui/core/TextField';
import Switch from '@material-ui/core/Switch';
import { orange } from '@material-ui/core/colors';
//End Material-UI

//MaterialUI configuration
const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    display: 'flex',
    padding: '8px',
    height: '100%',
    '& > * + *': {
      marginTop: theme.spacing(2),
    },
  },
  paper: {
    padding: theme.spacing(1),
    textAlign: 'center',
    color: theme.palette.text.secondary
  },
  formControl: {
    margin: theme.spacing(1),
    minWidth: '25%',
    height: '100%'
  },
  selectEmpty: {
    marginTop: theme.spacing(1),
  },
  menuButton: { 
    marginRight: theme.spacing(2),
  },
  menuTitle: {
    flexGrow: 1,
  },
  dataGrid: {

  },
  container: { 
    maxHeight: 440,
  },
}));
//End Material UI

function App() {

  const classes = useStyles();

  const takePic1 = () => {
    axios.get('http://localhost:3030/cam1').then(response => {
      console.log(response.data);
    })
  }

  const takePic2 = () => {
    axios.get('http://localhost:3030/cam2').then(response => {
      console.log(response.data);
    })
  }

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" className={classes.menuTitle}>
            Water plants project
          </Typography>
          <Button color="inherit" onClick={takePic1}> Camera 1 </Button>
          <Button color="inherit" onClick={takePic2}> Camera 2 </Button>
        </Toolbar>
      </AppBar>
      <Grid container spacing={2}>
        <Grid item xs={12}>

        </Grid>
      </Grid>
    </div>
  );
}

export default App;
